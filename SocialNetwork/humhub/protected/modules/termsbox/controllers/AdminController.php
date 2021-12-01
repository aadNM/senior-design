<?php

namespace humhub\modules\termsbox\controllers;

use Yii;
use yii\helpers\Url;
use humhub\modules\admin\components\Controller;

class AdminController extends Controller
{

    /**
     * Configuration Action for Super Admins
     */
    public function actionIndex()
    {
        $form = new \humhub\modules\termsbox\models\forms\EditForm();
        
        if ($form->load(Yii::$app->request->post()) && $form->validate() && $form->save()) {
            return $this->redirect(Url::to(['/termsbox/admin/index']));
        }

        return $this->render('index', ['model' => $form]);
    }

}

?>
