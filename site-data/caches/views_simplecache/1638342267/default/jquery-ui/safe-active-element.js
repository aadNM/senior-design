(function(factory){if(typeof define==="function"&&define.amd){define("jquery-ui/safe-active-element",["jquery","./version"],factory);}else{factory(jQuery);}}(function($){return $.ui.safeActiveElement=function(document){var activeElement;try{activeElement=document.activeElement;}catch(error){activeElement=document.body;}
if(!activeElement){activeElement=document.body;}
if(!activeElement.nodeName){activeElement=document.body;}
return activeElement;};}));