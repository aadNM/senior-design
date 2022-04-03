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
    nlu_regexes_endpoints = Blueprint("nlu_regexes_endpoints")

    @nlu_regexes_endpoints.route(
        "/projects/<project_id>/regexes", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped("regexes.list")
    async def get_regex_features(request: Request, project_id: Text) -> HTTPResponse:
        """Get the regular expressions for a project."""

        limit = common_utils.int_arg(request, "limit")
        offset = common_utils.int_arg(request, "offset", 0)

        data_service = DataService.from_request(request)
        regexes = data_service.get_regex_features(
            project_id, offset=offset, limit=limit
        )

        return response.json(regexes.result, headers={"X-Total-Count": regexes.count})

    @nlu_regexes_endpoints.route("/projects/<project_id>/regexes", methods=["POST"])
    @rasa_x_scoped("regexes.create")
    @validate_schema("regex")
    async def create_regular_expression(
        request: Request, project_id: Text
    ) -> HTTPResponse:
        """Get the regular expressions for a project."""

        data_service = DataService.from_request(request)
        try:
            created = data_service.create_regex_feature(request.json, project_id)
            return response.json(created, status=HTTPStatus.CREATED)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.BAD_REQUEST,
                "CreatingRegexFailed",
                "Failed to create regex.",
                details=e,
            )

    @nlu_regexes_endpoints.route(
        "/projects/<project_id>/regexes/<regex_id:int>", methods=["GET", "HEAD"]
    )
    @rasa_x_scoped("regexes.get")
    async def get_regex_feature_by_id(
        request: Request, project_id: Text, regex_id: int
    ) -> HTTPResponse:
        """Get regular expression by its id."""

        data_service = DataService.from_request(request)
        try:
            regex = data_service.get_regex_feature_by_id(regex_id)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.NOT_FOUND,
                "GetRegexFailed",
                "Failed to get regex by id.",
                details=e,
            )

        return response.json(regex)

    @nlu_regexes_endpoints.route(
        "/projects/<project_id>/regexes/<regex_id:int>", methods=["PUT"]
    )
    @rasa_x_scoped("regexes.update")
    @validate_schema("regex")
    async def update_regex_feature(
        request: Request, project_id: Text, regex_id: int
    ) -> HTTPResponse:
        """Update an existing regular expressions."""

        data_service = DataService.from_request(request)
        try:
            updated = data_service.update_regex_feature(regex_id, request.json)
            return response.json(updated)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.NOT_FOUND,
                "UpdatingRegexFailed",
                "Failed to update regex.",
                details=e,
            )

    @nlu_regexes_endpoints.route(
        "/projects/<project_id>/regexes/<regex_id:int>", methods=["DELETE"]
    )
    @rasa_x_scoped("regexes.delete")
    async def delete_regex_feature(
        request: Request, project_id: Text, regex_id: int
    ) -> HTTPResponse:
        """Delete regular expression by its id."""

        data_service = DataService.from_request(request)
        try:
            data_service.delete_regex_feature(regex_id)
        except ValueError as e:
            logger.error(e)
            return common_utils.error(
                HTTPStatus.NOT_FOUND,
                "DeletingRegexFailed",
                "Failed to delete regex by id.",
                details=e,
            )

        return response.text("", status=HTTPStatus.NO_CONTENT)

    return nlu_regexes_endpoints
