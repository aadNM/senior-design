<?php

namespace humhub\modules\termsbox;

use Yii;
use yii\helpers\Url;
use humhub\modules\user\models\User;

class Module extends \humhub\components\Module
{

    /**
     * Checks if the termsbox should be shown
     * 
     * @param User $user|null the user, if null the current logged in user will be used
     * @return boolean
     */
    public static function showTerms(User $user = null)
    {
        if (Yii::$app->user->isGuest) {
            return false;
        }
        
        if (!Yii::$app->getModule('termsbox')->settings->get('active')) {
            return false;
        }

        if ($user === null && !Yii::$app->user->isGuest) {
            $user = Yii::$app->user->getIdentity();
        }

        if ($user && $user->mustChangePassword()) {
            return false;
        }

        if ($user === null || empty($user->termsbox_accepted)) {
            return true;
        }

        return false;
    }

    public function hideNotAcceptedMembers()
    {
        if (!Yii::$app->getModule('termsbox')->settings->get('active')) {
            return false;
        }

        return (boolean) $this->settings->get('hideUnaccepted', false);
    }

    /**
     * @inheritdoc
     */
    public function getConfigUrl()
    {
        return Url::to(['/termsbox/admin/index']);
    }

}
