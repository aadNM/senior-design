<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit67282aec7b2ab9a8e40f65d8dc8ae12a
{
    public static $files = array (
        '383eaff206634a77a1be54e64e6459c7' => __DIR__ . '/..' . '/sabre/uri/lib/functions.php',
        '3569eecfeed3bcf0bad3c998a494ecb8' => __DIR__ . '/..' . '/sabre/xml/lib/Deserializer/functions.php',
        '93aa591bc4ca510c520999e34229ee79' => __DIR__ . '/..' . '/sabre/xml/lib/Serializer/functions.php',
    );

    public static $prefixLengthsPsr4 = array (
        'S' => 
        array (
            'Sabre\\Xml\\' => 10,
            'Sabre\\VObject\\' => 14,
            'Sabre\\Uri\\' => 10,
        ),
        'R' => 
        array (
            'Recurr\\' => 7,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Sabre\\Xml\\' => 
        array (
            0 => __DIR__ . '/..' . '/sabre/xml/lib',
        ),
        'Sabre\\VObject\\' => 
        array (
            0 => __DIR__ . '/..' . '/sabre/vobject/lib',
        ),
        'Sabre\\Uri\\' => 
        array (
            0 => __DIR__ . '/..' . '/sabre/uri/lib',
        ),
        'Recurr\\' => 
        array (
            0 => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr',
        ),
    );

    public static $prefixesPsr0 = array (
        'D' => 
        array (
            'Doctrine\\Common\\Collections\\' => 
            array (
                0 => __DIR__ . '/..' . '/doctrine/collections/lib',
            ),
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
        'Doctrine\\Common\\Collections\\AbstractLazyCollection' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/AbstractLazyCollection.php',
        'Doctrine\\Common\\Collections\\ArrayCollection' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/ArrayCollection.php',
        'Doctrine\\Common\\Collections\\Collection' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Collection.php',
        'Doctrine\\Common\\Collections\\Criteria' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Criteria.php',
        'Doctrine\\Common\\Collections\\Expr\\ClosureExpressionVisitor' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/ClosureExpressionVisitor.php',
        'Doctrine\\Common\\Collections\\Expr\\Comparison' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/Comparison.php',
        'Doctrine\\Common\\Collections\\Expr\\CompositeExpression' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/CompositeExpression.php',
        'Doctrine\\Common\\Collections\\Expr\\Expression' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/Expression.php',
        'Doctrine\\Common\\Collections\\Expr\\ExpressionVisitor' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/ExpressionVisitor.php',
        'Doctrine\\Common\\Collections\\Expr\\Value' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Expr/Value.php',
        'Doctrine\\Common\\Collections\\ExpressionBuilder' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/ExpressionBuilder.php',
        'Doctrine\\Common\\Collections\\Selectable' => __DIR__ . '/..' . '/doctrine/collections/lib/Doctrine/Common/Collections/Selectable.php',
        'Recurr\\DateExclusion' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/DateExclusion.php',
        'Recurr\\DateInclusion' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/DateInclusion.php',
        'Recurr\\DateInfo' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/DateInfo.php',
        'Recurr\\DateUtil' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/DateUtil.php',
        'Recurr\\DaySet' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/DaySet.php',
        'Recurr\\Exception' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Exception.php',
        'Recurr\\Exception\\InvalidArgument' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Exception/InvalidArgument.php',
        'Recurr\\Exception\\InvalidRRule' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Exception/InvalidRRule.php',
        'Recurr\\Exception\\InvalidWeekday' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Exception/InvalidWeekday.php',
        'Recurr\\Frequency' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Frequency.php',
        'Recurr\\Recurrence' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Recurrence.php',
        'Recurr\\RecurrenceCollection' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/RecurrenceCollection.php',
        'Recurr\\Rule' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Rule.php',
        'Recurr\\Time' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Time.php',
        'Recurr\\Transformer\\ArrayTransformer' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/ArrayTransformer.php',
        'Recurr\\Transformer\\ArrayTransformerConfig' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/ArrayTransformerConfig.php',
        'Recurr\\Transformer\\Constraint' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/Constraint.php',
        'Recurr\\Transformer\\ConstraintInterface' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/ConstraintInterface.php',
        'Recurr\\Transformer\\Constraint\\AfterConstraint' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/Constraint/AfterConstraint.php',
        'Recurr\\Transformer\\Constraint\\BeforeConstraint' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/Constraint/BeforeConstraint.php',
        'Recurr\\Transformer\\Constraint\\BetweenConstraint' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/Constraint/BetweenConstraint.php',
        'Recurr\\Transformer\\TextTransformer' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/TextTransformer.php',
        'Recurr\\Transformer\\Translator' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/Translator.php',
        'Recurr\\Transformer\\TranslatorInterface' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Transformer/TranslatorInterface.php',
        'Recurr\\Weekday' => __DIR__ . '/..' . '/simshaun/recurr/src/Recurr/Weekday.php',
        'Sabre\\Uri\\InvalidUriException' => __DIR__ . '/..' . '/sabre/uri/lib/InvalidUriException.php',
        'Sabre\\Uri\\Version' => __DIR__ . '/..' . '/sabre/uri/lib/Version.php',
        'Sabre\\VObject\\BirthdayCalendarGenerator' => __DIR__ . '/..' . '/sabre/vobject/lib/BirthdayCalendarGenerator.php',
        'Sabre\\VObject\\Cli' => __DIR__ . '/..' . '/sabre/vobject/lib/Cli.php',
        'Sabre\\VObject\\Component' => __DIR__ . '/..' . '/sabre/vobject/lib/Component.php',
        'Sabre\\VObject\\Component\\Available' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/Available.php',
        'Sabre\\VObject\\Component\\VAlarm' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VAlarm.php',
        'Sabre\\VObject\\Component\\VAvailability' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VAvailability.php',
        'Sabre\\VObject\\Component\\VCalendar' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VCalendar.php',
        'Sabre\\VObject\\Component\\VCard' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VCard.php',
        'Sabre\\VObject\\Component\\VEvent' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VEvent.php',
        'Sabre\\VObject\\Component\\VFreeBusy' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VFreeBusy.php',
        'Sabre\\VObject\\Component\\VJournal' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VJournal.php',
        'Sabre\\VObject\\Component\\VTimeZone' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VTimeZone.php',
        'Sabre\\VObject\\Component\\VTodo' => __DIR__ . '/..' . '/sabre/vobject/lib/Component/VTodo.php',
        'Sabre\\VObject\\DateTimeParser' => __DIR__ . '/..' . '/sabre/vobject/lib/DateTimeParser.php',
        'Sabre\\VObject\\Document' => __DIR__ . '/..' . '/sabre/vobject/lib/Document.php',
        'Sabre\\VObject\\ElementList' => __DIR__ . '/..' . '/sabre/vobject/lib/ElementList.php',
        'Sabre\\VObject\\EofException' => __DIR__ . '/..' . '/sabre/vobject/lib/EofException.php',
        'Sabre\\VObject\\FreeBusyData' => __DIR__ . '/..' . '/sabre/vobject/lib/FreeBusyData.php',
        'Sabre\\VObject\\FreeBusyGenerator' => __DIR__ . '/..' . '/sabre/vobject/lib/FreeBusyGenerator.php',
        'Sabre\\VObject\\ITip\\Broker' => __DIR__ . '/..' . '/sabre/vobject/lib/ITip/Broker.php',
        'Sabre\\VObject\\ITip\\ITipException' => __DIR__ . '/..' . '/sabre/vobject/lib/ITip/ITipException.php',
        'Sabre\\VObject\\ITip\\Message' => __DIR__ . '/..' . '/sabre/vobject/lib/ITip/Message.php',
        'Sabre\\VObject\\ITip\\SameOrganizerForAllComponentsException' => __DIR__ . '/..' . '/sabre/vobject/lib/ITip/SameOrganizerForAllComponentsException.php',
        'Sabre\\VObject\\InvalidDataException' => __DIR__ . '/..' . '/sabre/vobject/lib/InvalidDataException.php',
        'Sabre\\VObject\\Node' => __DIR__ . '/..' . '/sabre/vobject/lib/Node.php',
        'Sabre\\VObject\\PHPUnitAssertions' => __DIR__ . '/..' . '/sabre/vobject/lib/PHPUnitAssertions.php',
        'Sabre\\VObject\\Parameter' => __DIR__ . '/..' . '/sabre/vobject/lib/Parameter.php',
        'Sabre\\VObject\\ParseException' => __DIR__ . '/..' . '/sabre/vobject/lib/ParseException.php',
        'Sabre\\VObject\\Parser\\Json' => __DIR__ . '/..' . '/sabre/vobject/lib/Parser/Json.php',
        'Sabre\\VObject\\Parser\\MimeDir' => __DIR__ . '/..' . '/sabre/vobject/lib/Parser/MimeDir.php',
        'Sabre\\VObject\\Parser\\Parser' => __DIR__ . '/..' . '/sabre/vobject/lib/Parser/Parser.php',
        'Sabre\\VObject\\Parser\\XML' => __DIR__ . '/..' . '/sabre/vobject/lib/Parser/XML.php',
        'Sabre\\VObject\\Parser\\XML\\Element\\KeyValue' => __DIR__ . '/..' . '/sabre/vobject/lib/Parser/XML/Element/KeyValue.php',
        'Sabre\\VObject\\Property' => __DIR__ . '/..' . '/sabre/vobject/lib/Property.php',
        'Sabre\\VObject\\Property\\Binary' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Binary.php',
        'Sabre\\VObject\\Property\\Boolean' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Boolean.php',
        'Sabre\\VObject\\Property\\FlatText' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/FlatText.php',
        'Sabre\\VObject\\Property\\FloatValue' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/FloatValue.php',
        'Sabre\\VObject\\Property\\ICalendar\\CalAddress' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/CalAddress.php',
        'Sabre\\VObject\\Property\\ICalendar\\Date' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/Date.php',
        'Sabre\\VObject\\Property\\ICalendar\\DateTime' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/DateTime.php',
        'Sabre\\VObject\\Property\\ICalendar\\Duration' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/Duration.php',
        'Sabre\\VObject\\Property\\ICalendar\\Period' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/Period.php',
        'Sabre\\VObject\\Property\\ICalendar\\Recur' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/ICalendar/Recur.php',
        'Sabre\\VObject\\Property\\IntegerValue' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/IntegerValue.php',
        'Sabre\\VObject\\Property\\Text' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Text.php',
        'Sabre\\VObject\\Property\\Time' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Time.php',
        'Sabre\\VObject\\Property\\Unknown' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Unknown.php',
        'Sabre\\VObject\\Property\\Uri' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/Uri.php',
        'Sabre\\VObject\\Property\\UtcOffset' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/UtcOffset.php',
        'Sabre\\VObject\\Property\\VCard\\Date' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/VCard/Date.php',
        'Sabre\\VObject\\Property\\VCard\\DateAndOrTime' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/VCard/DateAndOrTime.php',
        'Sabre\\VObject\\Property\\VCard\\DateTime' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/VCard/DateTime.php',
        'Sabre\\VObject\\Property\\VCard\\LanguageTag' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/VCard/LanguageTag.php',
        'Sabre\\VObject\\Property\\VCard\\TimeStamp' => __DIR__ . '/..' . '/sabre/vobject/lib/Property/VCard/TimeStamp.php',
        'Sabre\\VObject\\Reader' => __DIR__ . '/..' . '/sabre/vobject/lib/Reader.php',
        'Sabre\\VObject\\Recur\\EventIterator' => __DIR__ . '/..' . '/sabre/vobject/lib/Recur/EventIterator.php',
        'Sabre\\VObject\\Recur\\MaxInstancesExceededException' => __DIR__ . '/..' . '/sabre/vobject/lib/Recur/MaxInstancesExceededException.php',
        'Sabre\\VObject\\Recur\\NoInstancesException' => __DIR__ . '/..' . '/sabre/vobject/lib/Recur/NoInstancesException.php',
        'Sabre\\VObject\\Recur\\RDateIterator' => __DIR__ . '/..' . '/sabre/vobject/lib/Recur/RDateIterator.php',
        'Sabre\\VObject\\Recur\\RRuleIterator' => __DIR__ . '/..' . '/sabre/vobject/lib/Recur/RRuleIterator.php',
        'Sabre\\VObject\\Settings' => __DIR__ . '/..' . '/sabre/vobject/lib/Settings.php',
        'Sabre\\VObject\\Splitter\\ICalendar' => __DIR__ . '/..' . '/sabre/vobject/lib/Splitter/ICalendar.php',
        'Sabre\\VObject\\Splitter\\SplitterInterface' => __DIR__ . '/..' . '/sabre/vobject/lib/Splitter/SplitterInterface.php',
        'Sabre\\VObject\\Splitter\\VCard' => __DIR__ . '/..' . '/sabre/vobject/lib/Splitter/VCard.php',
        'Sabre\\VObject\\StringUtil' => __DIR__ . '/..' . '/sabre/vobject/lib/StringUtil.php',
        'Sabre\\VObject\\TimeZoneUtil' => __DIR__ . '/..' . '/sabre/vobject/lib/TimeZoneUtil.php',
        'Sabre\\VObject\\UUIDUtil' => __DIR__ . '/..' . '/sabre/vobject/lib/UUIDUtil.php',
        'Sabre\\VObject\\VCardConverter' => __DIR__ . '/..' . '/sabre/vobject/lib/VCardConverter.php',
        'Sabre\\VObject\\Version' => __DIR__ . '/..' . '/sabre/vobject/lib/Version.php',
        'Sabre\\VObject\\Writer' => __DIR__ . '/..' . '/sabre/vobject/lib/Writer.php',
        'Sabre\\Xml\\ContextStackTrait' => __DIR__ . '/..' . '/sabre/xml/lib/ContextStackTrait.php',
        'Sabre\\Xml\\Element' => __DIR__ . '/..' . '/sabre/xml/lib/Element.php',
        'Sabre\\Xml\\Element\\Base' => __DIR__ . '/..' . '/sabre/xml/lib/Element/Base.php',
        'Sabre\\Xml\\Element\\Cdata' => __DIR__ . '/..' . '/sabre/xml/lib/Element/Cdata.php',
        'Sabre\\Xml\\Element\\Elements' => __DIR__ . '/..' . '/sabre/xml/lib/Element/Elements.php',
        'Sabre\\Xml\\Element\\KeyValue' => __DIR__ . '/..' . '/sabre/xml/lib/Element/KeyValue.php',
        'Sabre\\Xml\\Element\\Uri' => __DIR__ . '/..' . '/sabre/xml/lib/Element/Uri.php',
        'Sabre\\Xml\\Element\\XmlFragment' => __DIR__ . '/..' . '/sabre/xml/lib/Element/XmlFragment.php',
        'Sabre\\Xml\\LibXMLException' => __DIR__ . '/..' . '/sabre/xml/lib/LibXMLException.php',
        'Sabre\\Xml\\ParseException' => __DIR__ . '/..' . '/sabre/xml/lib/ParseException.php',
        'Sabre\\Xml\\Reader' => __DIR__ . '/..' . '/sabre/xml/lib/Reader.php',
        'Sabre\\Xml\\Service' => __DIR__ . '/..' . '/sabre/xml/lib/Service.php',
        'Sabre\\Xml\\Version' => __DIR__ . '/..' . '/sabre/xml/lib/Version.php',
        'Sabre\\Xml\\Writer' => __DIR__ . '/..' . '/sabre/xml/lib/Writer.php',
        'Sabre\\Xml\\XmlDeserializable' => __DIR__ . '/..' . '/sabre/xml/lib/XmlDeserializable.php',
        'Sabre\\Xml\\XmlSerializable' => __DIR__ . '/..' . '/sabre/xml/lib/XmlSerializable.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit67282aec7b2ab9a8e40f65d8dc8ae12a::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit67282aec7b2ab9a8e40f65d8dc8ae12a::$prefixDirsPsr4;
            $loader->prefixesPsr0 = ComposerStaticInit67282aec7b2ab9a8e40f65d8dc8ae12a::$prefixesPsr0;
            $loader->classMap = ComposerStaticInit67282aec7b2ab9a8e40f65d8dc8ae12a::$classMap;

        }, null, ClassLoader::class);
    }
}
