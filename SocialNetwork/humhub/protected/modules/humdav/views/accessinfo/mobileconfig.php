<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

use humhub\modules\humdav\components\UUIDHelper;
use yii\web\ForbiddenHttpException;
use yii\web\BadRequestHttpException;
use yii\helpers\Url;

$currentIdentity = Yii::$app->user->identity;
if ($currentIdentity === null) {
	throw new ForbiddenHttpException('You\'re not signed in.');
}

$targetDevice = Yii::$app->request->get('target');
if (!in_array($targetDevice, ['ios', 'osx'])) {
	throw new BadRequestHttpException('"'.$targetDevice.'" is not a supported target.');
}

$secureRequests = Yii::$app->request->getIsSecureConnection() ? 'true': 'false';

$payloadVersion = 1;

$uniqueId = UUIDHelper::generateNewFromStrings(Yii::$app->settings->get('name'), $currentIdentity->username, 'HumDAV');
$uniqueCardDavId = UUIDHelper::generateNewFromStrings('CardDAV', $uniqueId);
$uniqueCalDavId = UUIDHelper::generateNewFromStrings('CalDAV', $uniqueId);

$mobileconfig = '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>CardDAVAccountDescription</key>
			<string>'.Yii::$app->settings->get('name').' CardDAV</string>
			<key>CardDAVHostName</key>
			<string>'.Yii::$app->request->getHostName().'</string>
			<key>CardDAVPort</key>
			<integer>'.Yii::$app->request->getServerPort().'</integer>
			<key>CardDAVPrincipalURL</key>
			<string>'.Url::to('/humdav/remote/addressbooks/'.$currentIdentity->username.'/', $targetDevice === 'ios').'</string>
			<key>CardDAVUseSSL</key>
            <'.$secureRequests.'/>
            <key>CardDAVUsername</key>
            <string>'.$currentIdentity->username.'</string>
			<key>PayloadDescription</key>
			<string>CardDAV Configuration</string>
			<key>PayloadDisplayName</key>
			<string>'.$currentIdentity->username.' CardDAV</string>
			<key>PayloadIdentifier</key>
			<string>com.humdav.setup.carddav.'.$uniqueCardDavId.'</string>
			<key>PayloadOrganization</key>
			<string></string>
			<key>PayloadType</key>
			<string>com.apple.carddav.account</string>
			<key>PayloadUUID</key>
			<string>'.$uniqueCardDavId.'</string>
			<key>PayloadVersion</key>
			<integer>'.$payloadVersion.'</integer>
		</dict>
		<dict>
			<key>CalDAVAccountDescription</key>
			<string>'.Yii::$app->settings->get('name').' CalDAV</string>
			<key>CalDAVHostName</key>
			<string>'.Yii::$app->request->getHostName().'</string>
			<key>CalDAVPort</key>
			<integer>'.Yii::$app->request->getServerPort().'</integer>
			<key>CalDAVPrincipalURL</key>
			<string>'.Url::to('/humdav/remote/principals/'.$currentIdentity->username.'/', $targetDevice === 'ios').'</string>
			<key>CalDAVUseSSL</key>
            <'.$secureRequests.'/>
			<key>CalDAVUsername</key>
            <string>'.$currentIdentity->username.'</string>
			<key>PayloadDescription</key>
			<string>CalDAV Configuration</string>
			<key>PayloadDisplayName</key>
			<string>'.$currentIdentity->username.' CalDAV</string>
			<key>PayloadIdentifier</key>
			<string>com.humdav.setup.caldav.'.$uniqueCalDavId.'</string>
			<key>PayloadOrganization</key>
			<string></string>
			<key>PayloadType</key>
			<string>com.apple.caldav.account</string>
			<key>PayloadUUID</key>
			<string>'.$uniqueCalDavId.'</string>
			<key>PayloadVersion</key>
			<integer>'.$payloadVersion.'</integer>
		</dict>
	</array>
	<key>PayloadDescription</key>
	<string>Configuration profiles for the resources of the HumHub page '.Yii::$app->settings->get('name').'.</string>
	<key>PayloadDisplayName</key>
	<string>'.Yii::$app->settings->get('name').' HumDAV Configuration</string>
	<key>PayloadIdentifier</key>
	<string>com.humdav.setup.'.$uniqueId.'</string>
	<key>PayloadOrganization</key>
	<string></string>
	<key>PayloadRemovalDisallowed</key>
	<false/>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>'.$uniqueId.'</string>
	<key>PayloadVersion</key>
	<integer>'.$payloadVersion.'</integer>
</dict>
</plist>';

header('Content-Type: application/x-apple-aspen-config');
header('Content-Disposition: attachment; filename='.$currentIdentity->username.'-profile.mobileconfig'); 
header('Cache-Control: no-store');
header('Content-Length: '.strlen($mobileconfig));

echo $mobileconfig;
die();