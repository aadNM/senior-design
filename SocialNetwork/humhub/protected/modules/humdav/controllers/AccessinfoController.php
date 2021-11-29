<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\controllers;

use Yii;
use humhub\components\Controller;
use humhub\components\Response;
use yii\web\NotFoundHttpException;
use yii\web\ForbiddenHttpException;

class AccessinfoController extends Controller {
    /**
     * @inheritdoc
     */
    public function beforeAction($action) {
        $currentIdentity = Yii::$app->user->identity;
        if ($currentIdentity === null || Yii::$app->user->isGuest) {
            throw new ForbiddenHttpException('You\'re not signed in.');
        }
        
        $settings = Yii::$app->getModule('humdav')->settings;
        if ((boolean)$settings->get('active', false) !== true) {
            throw new NotFoundHttpException('Module not activated');
        }
        
        $allowedUsers = array_filter((array)$settings->getSerialized('enabled_users'));
        if (!in_array($currentIdentity->guid, $allowedUsers) && !empty($allowedUsers)) {
            throw new ForbiddenHttpException('You\'re not allowed to enter this page.');
        }

        return parent::beforeAction($action);
    }

    public function actionIndex() {
        $settings = Yii::$app->getModule('humdav')->settings;

        return $this->render('index', [
            'instructionLocation' => $settings->get('instruction_location')
        ]);
    }

    public function actionMobileconfig() {
        Yii::$app->response->format = Response::FORMAT_RAW;
        $this->layout = false;
        
        return $this->render('mobileconfig');
    }
}
