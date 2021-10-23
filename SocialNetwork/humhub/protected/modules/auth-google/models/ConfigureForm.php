<?php

namespace humhubContrib\auth\google\models;

use Yii;
use yii\base\Model;
use yii\helpers\Url;
use humhubContrib\auth\google\Module;

/**
 * The module configuration model
 */
class ConfigureForm extends Model
{
    /**
     * @var boolean Enable this authclient
     */
    public $enabled;

    /**
     * @var string the client id provided by Google
     */
    public $clientId;

    /**
     * @var string the client secret provided by Google
     */
    public $clientSecret;

    /**
     * @var string readonly
     */
    public $redirectUri;

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['clientId', 'clientSecret'], 'required'],
            [['enabled'], 'boolean'],
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'enabled' => Yii::t('AuthGoogleModule.base', 'Enabled'),
            'clientId' => Yii::t('AuthGoogleModule.base', 'Client ID'),
            'clientSecret' => Yii::t('AuthGoogleModule.base', 'Client secret'),
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeHints()
    {
        return [
        ];
    }

    /**
     * Loads the current module settings
     */
    public function loadSettings()
    {
        /** @var Module $module */
        $module = Yii::$app->getModule('auth-google');

        $settings = $module->settings;

        $this->enabled = (boolean)$settings->get('enabled');
        $this->clientId = $settings->get('clientId');
        $this->clientSecret = $settings->get('clientSecret');

        $this->redirectUri = Url::to(['/user/auth/external', 'authclient' => 'google'], true);
    }

    /**
     * Saves module settings
     */
    public function saveSettings()
    {
        /** @var Module $module */
        $module = Yii::$app->getModule('auth-google');

        $module->settings->set('enabled', (boolean)$this->enabled);
        $module->settings->set('clientId', $this->clientId);
        $module->settings->set('clientSecret', $this->clientSecret);

        return true;
    }

    /**
     * Returns a loaded instance of this configuration model
     */
    public static function getInstance()
    {
        $config = new static;
        $config->loadSettings();

        return $config;
    }

}
