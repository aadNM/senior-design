<?php

use yii\helpers\Html;
use yii\helpers\Url;
use humhub\widgets\ActiveForm;
use humhub\widgets\MarkdownField;
?>
<div class="panel panel-default">
    <div class="panel-heading"><?php echo Yii::t('TermsboxModule.views_admin_index', 'Terms Box Configuration'); ?></div>
    <div class="panel-body">

        <?php $form = ActiveForm::begin(); ?>

        <?= $form->field($model, 'active')->checkbox(); ?>
        <?= $form->field($model, 'title'); ?>
        <?= $form->field($model, 'statement'); ?>
        <?= $form->field($model, 'content')->widget(MarkdownField::class) ?>
        <?= $form->field($model, 'reset')->checkbox(); ?>
        <!--
        <?= $form->field($model, 'showAsModal')->checkbox(); ?>
        -->
        <?= $form->field($model, 'hideUnaccepted')->checkbox(); ?>

        <hr>

        <?= Html::submitButton(Yii::t('TermsboxModule.views_admin_index', 'Save'), ['class' => 'btn btn-primary', 'data-ui-loader' => '']); ?>
        <a class="btn btn-default" href="<?= Url::to(['/admin/module']); ?>"><?= Yii::t('TermsboxModule.views_admin_index', 'Back to modules'); ?></a>

        <?php ActiveForm::end(); ?>
    </div>
</div>