<?php

namespace humhub\modules\termsbox\controllers;

use Yii;
use humhub\components\Controller;

class IndexController extends Controller
{

    /**
     * @inheritdoc
     */
    public function getAccessRules()
    {
        return [
            ['login']
        ];
    }

    public function actionAccept()
    {
        $user = Yii::$app->user->getIdentity();
        $user->termsbox_accepted = true;
        $user->save();
        
        return $this->asJson(['success' => true]);
    }

    public function actionDecline()
    {
        $this->forcePostRequest();

        $user = Yii::$app->user->getIdentity();
        $user->termsbox_accepted = false;
        $user->save();

        // Note: don't use simple redirect because the logout action requires POST method
        return Yii::$app->runAction('/user/auth/logout');
    }

}
