<?php

namespace termsbox\functional;

use humhub\modules\termsbox\Module;
use termsbox\FunctionalTester;
use Yii;
use humhub\modules\termsbox\models\forms\EditForm;

class TermsboxCest
{

    /**
     * @var Module
     */
    var $module;

    public function _before()
    {
        $this->module = Yii::$app->getModule('termsbox');
        Yii::$app->cache->flush();
        $this->module->settings->delete('title');
        $this->module->settings->delete('content');
        $this->module->settings->delete('statement');
        $this->module->settings->delete('active');
        $this->module->settings->delete('showAsModal');
        $this->module->settings->delete('hideUnaccepted');
    }

    public function testTermsbox(FunctionalTester $I)
    {
        $I->amUser();
        $I->wantToTest('if the termsbox works as expected');
        $I->amGoingTo('save the termsbox form without activation');

        $form = new EditForm();
        $form->title = 'MyTitle';
        $form->statement = 'MyStatement';
        $form->active = false;
        $form->reset = true;
        $form->content = 'Test Message';
        $form->save();

        $I->expect('not to see the termbox');
        $I->dontSeeTermsbox();

        $I->amGoingTo('activate the termsbox form and check if I see the termsbox');
        $form->active = true;
        $form->reset = false;
        $form->save();
        $I->expectTo('see the termbox');
        $I->seeTermsbox();

        $I->amGoingTo('decline the termsbox');
        $I->declineTermsbox();
        $I->expect('an automatic logout');
        $I->see('Login');

        $I->amGoingTo('login and accept the termsbox');
        $I->amUser();
        $I->expectTo('see the termbox');
        $I->seeTermsbox();
        $I->acceptTermsbox();
        $I->expect('not to see the termbox after accepting it');
        $I->dontSeeTermsbox();

        // Note that the reset flag is ignored in this case
        $I->amGoingTo('save the termbox form again without activation but reset');
        $form->active = false;
        $form->save();
        $I->expect('not to see the termbox since it is not set to active');
        $I->dontSeeTermsbox();

        $I->amGoingTo('save the termbox form again with activation but no reset');
        $form->active = true;
        $form->reset = false;
        $form->save();
        $I->expect('not to see the termbox since I already accepted it before');
        $I->dontSeeTermsbox();

        $I->amGoingTo('save the termbox form again with activation and reset');
        $form->active = true;
        $form->reset = true;
        $form->save();
        $I->expect('to see the termbox since the reset was set to true');
        $I->seeTermsbox();
    }

}
