<?php

namespace gm\humhub\modules\scrollup\models;

use humhub\modules\ui\icon\widgets\Icon;
use Yii;
use yii\base\Model;

/**
 * ConfigureForm defines the configurable fields.
 */
class ConfigureForm extends Model
{

    const REGEX_COLOR = '/(#([0-9a-f]{3}){1,2}|(rgba|hsla)\(\d{1,3}%?(,\s?\d{1,3}%?){2},\s?(1|0?\.\d+)\)|(rgb|hsl)\(\d{1,3}%?(,\s?\d{1,3}%?\)){2})/';
    const REGEX_POSITION = '/(left|right|top|bottom) *: *([0-9]+) *(px|em|ex|%|in|cn|mm|pt|pc)/';

    public $position;

    public $color;

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            ['position', 'string'],
            ['position', 'validatePosition'],
            ['color', 'string'],
            ['color', 'validateColor'],
        ];
    }

    public function validateColor()
    {
        if(empty($this->color)) {
            return;
        }

        preg_match_all(static::REGEX_COLOR, $this->color, $matches, PREG_SET_ORDER);
        if(!isset($matches[0][0])) {
            $this->addError('color', Yii::t('ScrollupModule.config', 'Invalid color!'));
        } else {
            $this->color = $matches[0][0];
        }
    }

    public function validatePosition()
    {
        if(empty($this->position)) {
            return;
        }

        preg_match_all(static::REGEX_POSITION, $this->position, $matches, PREG_SET_ORDER);
        $result = '';
        $position = [];
        foreach ($matches as $match) {
            if(in_array($match[1], $position, true)) {
               continue;
            }

            $position[] = $match[1];
            $result .= $match[1].':'.$match[2].$match[3].';';
        }

        $this->position = $result;
    }

    public function getConfig()
    {
        $this->loadSettings();

        return [
            'buttonStyle' => $this->getStyle(),
            'isCustomPosition' => !empty($this->position),
            'icon' => Icon::get('chevron-up'),
            'scrollTop' => 300
        ];
    }

    public function getStyle()
    {
        $result = ['background-color' => $this->color];
        if(!empty($this->position)) {
            preg_match_all(static::REGEX_POSITION, $this->position, $matches, PREG_SET_ORDER);
            foreach ($matches as $match) {
                $result[$match[1]] = $match[2].$match[3];
            }
        }
        return $result;
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'position' =>  Yii::t('ScrollupModule.config','Position:'),
            'color' =>  Yii::t('ScrollupModule.config','Color:')
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeHints()
    {
        return [
            'position' => Yii::t('ScrollupModule.config','e.g: <code>left: 30px;</code> or <code>right: 30px;</code> (default: calculated center of stream sidebar)'),
            'color' => Yii::t('ScrollupModule.config', 'e.g. <code>#000000</code> (default: your themes @default color variable).')
        ];
    }

    public function loadSettings()
    {
        $this->position = Yii::$app->getModule('scrollup')->settings->get('position');
        $this->color = Yii::$app->getModule('scrollup')->settings->get('color', Yii::$app->getView()->theme->variable('default'));
        return true;
    }

    public function save()
    {
        if(!$this->validate()) {
            return false;
        }

        if(empty($this->color)) {
            $this->color = Yii::$app->getView()->theme->variable('default');
        }

        Yii::$app->getModule('scrollup')->settings->set('position', $this->position);

        Yii::$app->getModule('scrollup')->settings->set('color', $this->color);

        return true;
    }

}