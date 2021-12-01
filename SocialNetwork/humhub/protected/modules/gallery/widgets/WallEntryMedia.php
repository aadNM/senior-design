<?php

/**
 * @link https://www.humhub.org/
 * @copyright Copyright (c) 2015 HumHub GmbH & Co. KG
 * @license https://www.humhub.com/licences
 */

namespace humhub\modules\gallery\widgets;

use humhub\modules\content\widgets\stream\WallStreamModuleEntryWidget;
use humhub\modules\file\converter\PreviewImage;
use humhub\modules\gallery\models\Media;
use humhub\libs\MimeHelper;

/**
 * Widget that renders the Wallentry for a Media file.
 *
 * @package humhub.modules.gallery.widgets
 * @since 1.0
 * @author Sebastian Stumpf
 */
class WallEntryMedia extends WallStreamModuleEntryWidget
{

    /**
     * @inheritdoc
     */
    public $editRoute = "/gallery/media/edit";

    /**
     * @inheritdoc
     */
    public $editMode = self::EDIT_MODE_MODAL;

    /**
     * @var Media
     */
    public $model;

    /**
     * @inheritdoc
     */
    public function renderContent()
    {
        $media = $this->model;

        $galleryUrl = '#';
        $galleryName = null;
        if ($media->parentGallery !== null) {
            $galleryUrl = $media->parentGallery->getUrl();
            $galleryName = $media->parentGallery->title;
        }

        return $this->render('wallEntryMedia', [
                    'media' => $media,
                    'title' => $media->getTitle(),
                    'fileSize' => $media->getSize(),
                    'file' => $media->baseFile,
                    'previewImage' => new PreviewImage(),
                    'galleryUrl' => $galleryUrl,
                    'galleryName' => $galleryName,
                    'mimeIconClass' => MimeHelper::getMimeIconClassByExtension($media->baseFile)
        ]);
    }

    /**
     * Returns the edit url to edit the content (if supported)
     *
     * @return string url
     */
    public function getEditUrl()
    {
        if (parent::getEditUrl() === "") {
            return "";
        }
        if ($this->model instanceof Media) {
            return $this->model->getEditUrl(true);
        }
        return "";
    }

    /**
     * @return string a non encoded plain text title (no html allowed) used in the header of the widget
     */
    protected function getTitle()
    {
        return $this->model->title;
    }

}
