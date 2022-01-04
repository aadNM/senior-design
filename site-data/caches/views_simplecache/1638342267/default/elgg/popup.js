define('elgg/popup',['elgg','jquery','jquery-ui/position','jquery-ui/unique-id'],function(elgg,$){var popup={init:function(){$(document).on('click',function(e){if(e.isDefaultPrevented()){return;}
var $eventTargets=$(e.target).parents().addBack();if($eventTargets.is('.elgg-state-popped')){return;}
popup.close();});popup.init=elgg.nullFunction;},bind:function($triggers){$triggers.off('click.popup').on('click.popup',function(e){if(e.isDefaultPrevented()){return;}
e.preventDefault();e.stopPropagation();popup.open($(this));});},open:function($trigger,$target,position){if(typeof $trigger==='undefined'||!$trigger.length){return;}
if(typeof $target==='undefined'){var href=$trigger.attr('href')||$trigger.data('href')||'';var targetSelector=elgg.getSelectorFromUrlFragment(href);$target=$(targetSelector);}else{$target.uniqueId();var targetSelector='#'+$target.attr('id');}
if(!$target.length){return;}
var params={targetSelector:targetSelector,target:$target,source:$trigger};position=position||{my:'center top',at:'center bottom',of:$trigger,collision:'fit fit'};$.extend(position,$trigger.data('position'));position=elgg.trigger_hook('getOptions','ui.popup',params,position);if(!position){return;}
popup.init();if($target.is('.elgg-state-popped')){popup.close($target);return;}
popup.close();$target.data('trigger',$trigger);$target.data('position',position);if(!$trigger.is('.elgg-popup-inline')){$target.appendTo('body');$(document).one('scroll',function(){popup.close();});}
$target.position(position).fadeIn().addClass('elgg-state-active elgg-state-popped').position(position);$trigger.addClass('elgg-state-active');$target.trigger('open');},close:function($targets){if(typeof $targets==='undefined'){$targets=$('.elgg-state-popped');}
if(!$targets.length){return;}
$targets.each(function(){var $target=$(this);if(!$target.is(':visible')){return;}
var $trigger=$target.data('trigger');if($trigger.length){$trigger.removeClass('elgg-state-active');}
$target.fadeOut().removeClass('elgg-state-active elgg-state-popped');$target.trigger('close');});}};return popup;});