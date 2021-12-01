<?php

use kartik\widgets\ColorInput;
use yii\bootstrap\ActiveForm;
use yii\helpers\Html;
?>

<div class="panel panel-default">

    <div class="panel-heading"><?= \Yii::t('ScrollupModule.config', '<strong>Scroll Up</strong> module configuration'); ?></div>

    <div class="panel-body">

        <?php $form = ActiveForm::begin(['id' => 'configure-form']); ?>
        <div class="form-group">
            <?= $form->field($model, 'position'); ?>
            <?= $form->field($model, 'color')->widget(ColorInput::class, ['options' => ['placeholder' => \Yii::t('ScrollupModule.config', 'Select color ...')]]); ?>
        </div>

        <div class="form-group">
            <?= Html::submitButton(\Yii::t('ScrollupModule.config', 'Save'), ['class' => 'btn btn-primary', 'data-ui-loader' => '']); ?>
        </div>

        <?php ActiveForm::end(); ?>
    </div>
</div>
