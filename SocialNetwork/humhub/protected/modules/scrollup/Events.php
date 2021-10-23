<?php

namespace gm\humhub\modules\scrollup;

use Yii;
use yii\helpers\Url;
use yii\base\BaseObject;
use humhub\models\Setting;

class Events extends BaseObject
{
     /**
     * @param \yii\base\Event $event
     * @throws \Exception
     * @throws \Throwable
     */
    public static function onLayoutAddonsInit($event)
    {
        $event->sender->addWidget(widgets\ScrollUp::class);

    }
}