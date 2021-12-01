<?php

namespace gm\humhub\modules\scrollup;

use gm\humhub\modules\scrollup\models\ConfigureForm;
use humhub\modules\ui\icon\widgets\Icon;
use humhub\modules\ui\view\components\View;
use yii\web\AssetBundle;
use yii\web\JqueryAsset;

/**
 * Asset bundle for Scrollup
 *
 */
class Assets extends AssetBundle
{
    public $sourcePath = '@scrollup/assets';

    public $defer = true;

    public $css = [
        'css/scrollup.css',
    ];

    public $js = [
        'js/scrollup.js',
    ];

    /**
     * @param View $view
     * @return AssetBundle
     */
    public static function register($view)
    {
        $form = new ConfigureForm();
        $view->registerJsConfig('scrollUpButton', $form->getConfig());
        return parent::register($view);
    }

    public $depends = [
        JqueryAsset::class
    ];
}
