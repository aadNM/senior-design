<?php

namespace humhub\modules\termsbox\models\forms;

use humhub\models\ModuleEnabled;
use humhub\modules\file\components\FileManager;
use humhub\modules\file\libs\FileHelper;
use humhub\modules\file\models\File;
use Yii;
use humhub\modules\user\models\User;

class EditForm extends \yii\base\Model
{

    public $active;
    public $title;
    public $content;
    public $reset;
    public $statement;
    public $hideUnaccepted;
    public $showAsModal;

    /**
     * @inheritdocs
     */
    public function rules()
    {
        return array(
            array(['title', 'content', 'statement'], 'required'),
            array(['reset', 'active', 'hideUnaccepted', 'showAsModal'], 'safe')
        );
    }

    /**
     * @inheritdocs
     */
    public function init()
    {
        $settings = Yii::$app->getModule('termsbox')->settings;
        $this->title = $settings->get('title', Yii::t('TermsboxModule.models_forms_EditForm', 'Terms & Conditions'));
        $this->statement = $settings->get('statement', Yii::t('TermsboxModule.models_forms_EditForm', 'Please Read and Agree to our Terms & Conditions'));
        $this->content = $settings->get('content');
        $this->active = $settings->get('active', false);
        $this->showAsModal = $settings->get('showAsModal', false);
        $this->hideUnaccepted = $settings->get('hideUnaccepted', false);
    }

    /**
     * Declares customized attribute labels.
     * If not declared here, an attribute would have a label that is
     * the same as its name with the first letter in upper case.
     */
    public function attributeLabels()
    {
        return array(
            'active' => Yii::t('TermsboxModule.models_forms_EditForm', 'Active'),
            'title' => Yii::t('TermsboxModule.models_forms_EditForm', 'Title'),
            'statement' => Yii::t('TermsboxModule.models_forms_EditForm', 'Statement'),
            'content' => Yii::t('TermsboxModule.models_forms_EditForm', 'Content'),
            'reset' => Yii::t('TermsboxModule.models_forms_EditForm', 'Mark as unseen for all users'),
            'showAsModal' => Yii::t('TermsboxModule.models_forms_EditForm', 'Show terms as modal'),
            'hideUnaccepted' => Yii::t('TermsboxModule.models_forms_EditForm', 'Hide users which not accepted the terms (Note: May require search index rebuild)'),
        );
    }

    /**
     * Saves the given form settings.
     */
    public function save()
    {
        $settings = Yii::$app->getModule('termsbox')->settings;
        $settings->set('title', $this->title);
        $settings->set('statement', $this->statement);
        $settings->set('content', $this->content);
        $settings->set('active', (boolean) $this->active);
        $settings->set('showAsModal', (boolean) $this->showAsModal);
        $settings->set('hideUnaccepted', (boolean) $this->hideUnaccepted);

        $fileManager = new FileManager(['record' => ModuleEnabled::findOne((['module_id' => 'termsbox']))]);
        $fileManager->attach(Yii::$app->request->post('fileList'));

        if ($this->reset) {
            User::updateAll(['termsbox_accepted' => false]);
            if (!Yii::$app->user->isGuest) {
                Yii::$app->user->getIdentity()->termsbox_accepted = false;
            }
        }

        return true;
    }

}
