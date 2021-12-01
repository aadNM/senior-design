<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

use yii\helpers\Url;
use humhub\modules\directory\widgets\Menu;

\humhub\assets\JqueryKnobAsset::register($this);
?>

<div class="container">
    <div class="row">
        <?php if ($instructionLocation === 'directory_menu') { ?>
            <div class="col-md-2">
                <?= Menu::widget(); ?>
            </div>
        <?php } ?>

        <div class="<?= $instructionLocation === 'directory_menu' ? 'col-md-10' : 'col-md-12' ?>">
            <div class="panel">
                <div class="panel-heading"><i class="fa far fa-address-card"></i> <span><strong>HumDAV</strong> Access Infos</span></div>
                <div class="panel-body">
                    <p>
                        If you visit this page with iOS or macOS, you can download an automatically generated configuration file here:
                        <br>
                        <a class="btn btn-default" href="<?= Url::to(['/humdav/accessinfo/mobileconfig', 'target' => 'ios']); ?>" target="_blank">Download iOS Configuration File</a>
                        <a class="btn btn-default" href="<?= Url::to(['/humdav/accessinfo/mobileconfig', 'target' => 'osx']); ?>" target="_blank">Download macOS Configuration File</a>
                    </p>
                    <hr>
                    <p>
                        Otherwise you can enter the following configuration into your device (<a href="https://wiki.davical.org/index.php/CardDAV_Clients" target="_blank" rel="noopener noreferrer">List with some CardDAV clients</a>):
                        <dl>
                            <dt>Type:</dt>
                            <dd>CardDAV & CalDAV</dd>

                            <dt>CardDAV Url:</dt>
                            <dd><?=Url::to(['/humdav/remote/addressbooks/'.Yii::$app->user->identity->username.'/'], true)?></dd>

                            <dt>CalDAV Url:</dt>
                            <dd><?=Url::to(['/humdav/remote/calendars/'.Yii::$app->user->identity->username.'/'], true)?></dd>

                            <dt>Principal URL (=CalDAV Url for iOS and macOS):</dt>
                            <dd><?=Url::to(['/humdav/remote/principals/'.Yii::$app->user->identity->username.'/'], true)?></dd>

                            <dt>Username:</dt>
                            <dd><?=Yii::$app->user->identity->username?></dd>

                            <dt>Password:</dt>
                            <dd><i>Your HumHub Password</i></dd>

                            <dt>Auth Type:</dt>
                            <dd>Basic</dd>

                            <dt>Email:</dt>
                            <dd><?=Yii::$app->user->identity->email?></dd>
                        </dl>
                    </p>
                    <hr>
                    <p>
                        If authentication is not possible, this may have the following reasons:
                        <ul>
                            <li>The module has not been activated yet.</li>
                            <li>You have not been authorized for access.</li>
                            <li>You have a typo somewhere.</li>
                            <li>Also check the upper and lower case of your username.</li>
                        </ul>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
