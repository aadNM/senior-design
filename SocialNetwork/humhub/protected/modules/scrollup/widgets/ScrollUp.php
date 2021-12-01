<?php

namespace gm\humhub\modules\scrollup\widgets;

use humhub\components\Widget;
use Yii;
use gm\humhub\modules\scrollup\Assets;

/**
 * scroll-up widget to include in a website
 *
 */
class ScrollUp extends Widget
{
    /**
     * @inheritdoc
     */
    public function run()
    {
        $view = $this->getView();
        Assets::register($view);

        return '';
    }
}
