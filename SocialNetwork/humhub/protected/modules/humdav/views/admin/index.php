<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

use yii\helpers\Html;
use yii\helpers\Url;
use humhub\widgets\ActiveForm;
use humhub\modules\user\widgets\UserPickerField;
use humhub\modules\humdav\models\admin\EditForm;

?>

<div class="panel panel-default">
    <div class="panel-heading">HumHub DAV Access configuration</div>
    <div class="panel-body">

        <?php $form = ActiveForm::begin(); ?>

        <?= $form->field($model, 'active')->checkbox(); ?>
        
        <hr />

        <?= $form->field($model, 'instruction_location')->dropDownList(EditForm::getWidgetLocations()); ?>
        <?= $form->field($model, 'instruction_location_sort_order')->input('number', ['min' => 0]); ?>

        <hr />
        
        <?= $form->field($model, 'enabled_users')->widget(UserPickerField::class); ?>

        <hr />

        <?= $form->field($model, 'include_address')->checkbox(); ?>
        <?= $form->field($model, 'include_profile_image')->checkbox(); ?>
        <?= $form->field($model, 'include_birthday')->checkbox(); ?>
        <?= $form->field($model, 'include_gender')->checkbox(); ?>
        <?= $form->field($model, 'include_phone_numbers')->checkbox(); ?>
        <?= $form->field($model, 'include_url')->checkbox(); ?>

        <hr />

        <?= $form->field($model, 'enable_space_addressbooks')->checkbox(); ?>

        <hr />

        <?= $form->field($model, 'enable_browser_plugin')->checkbox(); ?>
        <?= $form->field($model, 'enable_auto_discovery')->checkbox(['disabled' => $auto_discovery_available !== true]); ?>

        <hr />

        <?= Html::submitButton("Save", ['class' => 'btn btn-primary', 'data-ui-loader' => '']); ?>
        <a class="btn btn-default" href="<?= Url::to(['/admin/module']); ?>">Back to modules</a>
        <a>This module is now available in the Marketplace.</a>

        <hr />

        <span>If you like this plugin, I would be very happy about a <a href="https://ko-fi.com/KeudellCoding" target="_blank" rel="noopener noreferrer">Ko-fi</a> :)</span>

        <?php ActiveForm::end(); ?>
    </div>
</div>