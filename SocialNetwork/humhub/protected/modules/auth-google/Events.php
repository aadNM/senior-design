<?php

namespace humhubContrib\auth\google;

use humhub\components\Event;
use humhub\modules\user\authclient\Collection;
use humhubContrib\auth\google\authclient\GoogleAuth;
use humhubContrib\auth\google\models\ConfigureForm;

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
            $authClientCollection->setClient('google', [
                'class' => GoogleAuth::class,
                'clientId' => ConfigureForm::getInstance()->clientId,
                'clientSecret' => ConfigureForm::getInstance()->clientSecret
            ]);
        }
    }

}