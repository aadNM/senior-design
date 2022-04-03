import logging
from http import HTTPStatus
from typing import Text

import rasax.community.utils.common as common_utils
from rasax.community.api.decorators import (
    rasa_x_scoped,
    validate_schema,
)
from rasax.community.services.data_service import DataService
from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse

logger = logging.getLogger(__name__)


def blueprint():
    nlu_lookup_tables_endpoints = Blueprint("nlu_lookup_tables_endpoints")

    @nlu_lookup_tables_endpoints.route(
        "/projects/<project_id>/lookupTables", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped("lookup_tables.list")
    async def get_lookup_tables(request: Request, project_id: Text) -> HTTPResponse:
        """Returns all lookup tables of a certain project.

        The returned objects do not contain the elements of the lookup tables, but
        the reference to the lookup table file.
        """

        data_service = DataService.from_request(request)
        lookup_tables = data_service.get_lookup_tables(project_id)

        return response.json(
            lookup_tables, headers={"X-Total-Count": len(lookup_tables)}
        )

    @nlu_lookup_tables_endpoints.route(
        "/projects/<project_id>/lookupTables/<lookup_table_id:int>",
        methods=["GET", "HEAD"],
    )
    @rasa_x_scoped("lookup_tables.get")
    async def get_lookup_table_content(
        request: Request, project_id: Text, lookup_table_id: int
    ) -> HTTPResponse:
        """Returns the content of a lookup table."""

        data_service = DataService.from_request(request)
        try:
            content = data_service.get_lookup_table(lookup_table_id)
            return response.text(content)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.NOT_FOUND,
                "GettingLookupTableFailed",
                f"Lookup table with id '{lookup_table_id}' does not exist.",
                details=e,
            )

    @nlu_lookup_tables_endpoints.route(
        "/projects/<project_id>/lookupTables", methods=["POST"]
    )
    @rasa_x_scoped("lookup_tables.create")
    @validate_schema("lookup_table")
    async def create_lookup_table(request: Request, project_id: Text) -> HTTPResponse:
        """Upload a lookup table."""

        lookup_table = request.json
        content = lookup_table["content"]
        content = common_utils.decode_base64(content)

        data_service = DataService.from_request(request)
        created = data_service.save_lookup_table(
            lookup_table["filename"], content, project_id
        )

        return response.json(created, status=HTTPStatus.CREATED)

    @nlu_lookup_tables_endpoints.route(
        "/projects/<project_id>/lookupTables/<lookup_table_id:int>", methods=["DELETE"]
    )
    @rasa_x_scoped("lookup_tables.delete")
    async def delete_lookup_table(
        request: Request, project_id: Text, lookup_table_id: int
    ) -> HTTPResponse:
        """Deletes a lookup table."""

        data_service = DataService.from_request(request)
        try:
            data_service.delete_lookup_table(lookup_table_id)
            return response.text("", HTTPStatus.NO_CONTENT)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.NOT_FOUND,
                "LookupTableDeletionFailed",
                f"Lookup table with id '{lookup_table_id}' does not exist.",
                details=e,
            )

    return nlu_lookup_tables_endpoints
