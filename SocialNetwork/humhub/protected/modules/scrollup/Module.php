<?php

namespace gm\humhub\modules\scrollup;

use yii\helpers\Url;
use humhub\components\Module as BaseModule;

class Module extends BaseModule
{

    /**
     * @inheritdoc
     */
    public function getConfigUrl()
    {
        return Url::to(['/scrollup/admin/index']);
    }
}