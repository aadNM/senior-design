<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\models\admin;

use humhub\modules\humdav\controllers\AdminController;
use Yii;
use yii\base\Model;

class EditForm extends Model {
    public $active;
    public $instruction_location;
    public $instruction_location_sort_order;
    public $enabled_users;
    public $include_address;
    public $include_profile_image;
    public $include_birthday;
    public $include_gender;
    public $include_phone_numbers;
    public $include_url;
    public $enable_space_addressbooks;
    public $enable_browser_plugin;
    public $enable_auto_discovery;

    /**
     * @inheritdocs
     */
    public function rules() {
        return [
            [['instruction_location'], 'in', 'range' => array_keys(static::getWidgetLocations())],
            [['instruction_location_sort_order'], 'number', 'min' => 0],
            [['active', 'enabled_users'], 'safe'],
            [['include_address', 'include_profile_image', 'include_birthday', 'include_gender', 'include_phone_numbers', 'include_url', 'enable_space_addressbooks', 'enable_browser_plugin', 'enable_auto_discovery'], 'boolean'],
            [['instruction_location_sort_order'], 'required']
        ];
    }

    /**
     * @inheritdocs
     */
    public function init() {
        $settings = Yii::$app->getModule('humdav')->settings;
        $this->active = $settings->get('active', false);

        $this->instruction_location = $settings->get('instruction_location');
        $this->instruction_location_sort_order = $settings->get('instruction_location_sort_order', 400);

        $this->enabled_users = (array)$settings->getSerialized('enabled_users');

        $this->include_address = $settings->get('include_address', true);
        $this->include_profile_image = $settings->get('include_profile_image', true);
        $this->include_birthday = $settings->get('include_birthday', true);
        $this->include_gender = $settings->get('include_gender', true);
        $this->include_phone_numbers = $settings->get('include_phone_numbers', true);
        $this->include_url = $settings->get('include_url', true);

        $this->enable_space_addressbooks = $settings->get('enable_space_addressbooks', true);
        
        $this->enable_browser_plugin = $settings->get('enable_browser_plugin', false);
        $this->enable_auto_discovery = AdminController::getAutoDiscoveryStatus();
    }

    /**
     * @inheritdocs
     */
    public function attributeLabels() {
        return [
            'active' => 'Enable Module',
            'enable_browser_plugin' => 'Enable Browser Access (not recommended)'
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeHints() {
        $result = [
            'enabled_users' => 'If empty, all users have access.'
        ];

        if (AdminController::autoDiscoveryAvailable()) {
            $result['enable_auto_discovery'] = '<b>IMPORTANT</b>: Please watch out for unexpected changes to the .htaccess file after an HumHub update. If errors occur, the current .htaccess file must be replaced with the <a href="https://github.com/humhub/humhub/blob/master/.htaccess.dist" target="_blank" ref="noopener noreferrer">current one from the official repo</a>.';
        }
        else if (!AdminController::autoDiscoveryReadable()) {
            $result['enable_auto_discovery'] = 'The .htaccess file cannot be read. The current auto discovery status is unknown.';
        }
        else if (!AdminController::autoDiscoveryWriteable()) {
            $result['enable_auto_discovery'] = 'The .htaccess file unfortunately can not be changed.';
        }

        return $result;
    }

    /**
     * Saves the given form settings.
     */
    public function save() {
        $settings = Yii::$app->getModule('humdav')->settings;
        $settings->set('active', (boolean) $this->active);

        $settings->set('instruction_location', $this->instruction_location);
        $settings->set('instruction_location_sort_order', $this->instruction_location_sort_order);

        $settings->setSerialized('enabled_users', (array)$this->enabled_users);

        $settings->set('include_address', (boolean) $this->include_address);
        $settings->set('include_profile_image', (boolean) $this->include_profile_image);
        $settings->set('include_birthday', (boolean) $this->include_birthday);
        $settings->set('include_gender', (boolean) $this->include_gender);
        $settings->set('include_phone_numbers', (boolean) $this->include_phone_numbers);
        $settings->set('include_url', (boolean) $this->include_url);

        $settings->set('enable_space_addressbooks', (boolean) $this->enable_space_addressbooks);
        
        $settings->set('enable_browser_plugin', (boolean) $this->enable_browser_plugin);
        AdminController::setAutoDiscoveryStatus((boolean) $this->enable_auto_discovery);

        return true;
    }

    public static function getWidgetLocations() {
        $result = [
            'dont_show' => 'Don\'t show (The module will work anyway)',
            'top_menu' => 'Top menu'
        ];

        if (version_compare(Yii::$app->version, '1.9.0', 'lt')) {
            $result['directory_menu'] = 'Directory menu (Not available as of HumHub version 1.9)';
        }

        return $result;
    }
}
