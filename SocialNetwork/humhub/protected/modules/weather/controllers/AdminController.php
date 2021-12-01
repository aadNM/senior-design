<?php

namespace gm\modules\weather\controllers;

use Yii;
use gm\modules\weather\models\ConfigureForm;
use humhub\modules\admin\components\Controller;

class AdminController extends Controller
{

    public function actionIndex()
    {
        $model = new ConfigureForm();
        $model->loadSettings();

        if ($model->load(Yii::$app->request->post()) && $model->save()) {
            $this->view->saved();
        }

        return $this->render('index', ['model' => $model]);
    }

}
