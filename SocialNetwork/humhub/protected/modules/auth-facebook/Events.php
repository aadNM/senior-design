<?php

namespace humhubContrib\auth\facebook;

use humhub\components\Event;
use humhub\modules\user\authclient\Collection;
use humhubContrib\auth\facebook\authclient\FacebookAuth;
use humhubContrib\auth\facebook\models\ConfigureForm;

class Events
{
    /**
     * @param Event $event
     */
    public static function onAuthClientCollectionInit($event)
    {
        /** @var Collection $authClientCollection */
        $authClientCollection = $event->sender;

        if (!empty(ConfigureForm::getInstance()->enabled)) {
            $authClientCollection->setClient('facebook', [
                'class' => FacebookAuth::class,
                'clientId' => ConfigureForm::getInstance()->clientId,
                'clientSecret' => ConfigureForm::getInstance()->clientSecret
            ]);
        }
    }

}
