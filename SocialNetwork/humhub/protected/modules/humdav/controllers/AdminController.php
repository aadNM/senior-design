<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\controllers;

use Yii;
use yii\helpers\Url;
use humhub\components\Response;
use humhub\modules\admin\components\Controller;
use humhub\modules\humdav\models\admin\EditForm;

class AdminController extends Controller {
    const REWRITE_RULE = 'RewriteRule ^\.well-known/(carddav|caldav) /humdav/remote/ [R=301,L]';
    const LINE_AFTER_REWRITE_RULE = 'RewriteRule .? %{ENV:BASE}/index.php [L]';
    const DISABLED_FILES_MATCH_LINE = '<FilesMatch "^(\.|composer\.(json|lock|phar)$)">';
    const ENABLED_FILES_MATCH_LINE = '<FilesMatch "^(\.(?!well-known)|composer\.(json|lock|phar)$)">';

    public function actionIndex() {
        Yii::$app->response->format = Response::FORMAT_HTML;

        $form = new EditForm();
        
        if ($form->load(Yii::$app->request->post()) && $form->validate() && $form->save()) {
            $this->view->saved();
            return $this->redirect(Url::to(['/humdav/admin/index']));
        }

        return $this->render('index', [
            'model' => $form,
            'auto_discovery_available' => self::autoDiscoveryAvailable()
        ]);
    }

    public static function autoDiscoveryWriteable() {
        $rootFolder = Yii::getAlias('@webroot');
        if (!is_writable($rootFolder)) {
            Yii::warning('Not writable: ' . $rootFolder, 'humdav');
            return false;
        }

        $htaccessFile = Yii::getAlias('@webroot/.htaccess');
        if (!is_writable($htaccessFile)) {
            Yii::warning('Not writable: ' . $htaccessFile, 'humdav');
            return false;
        }

        return true;
    }
    public static function autoDiscoveryReadable() {
        $htaccessFile = Yii::getAlias('@webroot/.htaccess');
        if (!is_readable($htaccessFile)) {
            Yii::warning('Not writable: ' . $htaccessFile, 'humdav');
            return false;
        }

        return true;
    }
    public static function autoDiscoveryAvailable() {
        return self::autoDiscoveryReadable() && self::autoDiscoveryWriteable();
    }

    public static function getAutoDiscoveryStatus() {
        if (!self::autoDiscoveryReadable()) {
            return false;
        }
        
        $rewriteRuleInFile = strpos(file_get_contents(Yii::getAlias('@webroot/.htaccess')), self::REWRITE_RULE) !== false;
        $filesMatchLineInFile = strpos(file_get_contents(Yii::getAlias('@webroot/.htaccess')), self::ENABLED_FILES_MATCH_LINE) !== false;

        return $rewriteRuleInFile && $filesMatchLineInFile;
    }
    public static function setAutoDiscoveryStatus(bool $enable) {
        if (!self::autoDiscoveryWriteable()) {
            return false;
        }
        if (self::getAutoDiscoveryStatus() === $enable) {
            return true;
        }

        if ($enable && !self::backupHtaccess()) {
            return false;
        }

        if ($enable) {
            if ($fileContent = file(Yii::getAlias('@webroot/.htaccess'))) {
                foreach($fileContent as $rowNumber => $rowContent) {
                    if (strpos($rowContent, self::LINE_AFTER_REWRITE_RULE) !== false) {
                        array_splice($fileContent, $rowNumber, 0, "    ".self::REWRITE_RULE."\n");
                    }
                }
                foreach($fileContent as $rowNumber => $rowContent) {
                    if (strpos($rowContent, self::DISABLED_FILES_MATCH_LINE) !== false) {
                        $fileContent[$rowNumber] = self::ENABLED_FILES_MATCH_LINE."\n";
                    }
                }
            }
            
            return file_put_contents(Yii::getAlias('@webroot/.htaccess'), $fileContent) !== false;
        }
        else {
            return self::restoreHtaccess();
        }
    }

    public static function backupHtaccess() {
        if (!self::autoDiscoveryWriteable()) {
            return false;
        }
        return copy(Yii::getAlias('@webroot/.htaccess'), Yii::getAlias('@webroot/.htaccess.humdav.backup'));
    }
    public static function restoreHtaccess() {
        if (!self::autoDiscoveryWriteable()) {
            return false;
        }

        if (!file_exists(Yii::getAlias('@webroot/.htaccess.humdav.backup'))) {
            return false;
        }

        if (!copy(Yii::getAlias('@webroot/.htaccess.humdav.backup'), Yii::getAlias('@webroot/.htaccess'))) {
            return false;
        }
        return unlink(Yii::getAlias('@webroot/.htaccess.humdav.backup'));
    }
}
