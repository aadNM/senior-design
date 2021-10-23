<?php

namespace humhub\modules\termsbox;

use Yii;
use humhub\modules\user\events\UserEvent;
use humhub\events\ActiveQueryEvent;

/**
 * Termsbox Event Handling
 *
 * @author luke
 */
class Events
{

    /**
     * On Init of Dashboard Sidebar, add the widget
     *
     * @param type $event
     */
    public static function onLayoutAddonsInit($event)
    {
        if (Yii::$app->getModule('termsbox')->showTerms()) {
            $event->sender->addWidget(widgets\TermsboxModal::className(), [], ['sortOrder' => 99999]);
        }
    }

    public static function onUserModelIsVisible(UserEvent $event)
    {
        if (Yii::$app->getModule('termsbox')->hideNotAcceptedMembers() && empty($event->user->termsbox_accepted)) {
            $event->result['isVisible'] = false;
        }
    }

    public static function onUserQueryVisible(ActiveQueryEvent $event)
    {
        if (Yii::$app->getModule('termsbox')->hideNotAcceptedMembers()) {
            $event->query->andWhere(['user.termsbox_accepted' => 1]);
        }
    }

}
