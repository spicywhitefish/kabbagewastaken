jQuery.extend({
    getQueryParameters : function(str) {
	    return (str || document.location.search).replace(/(^\?)/,'').split("&").map(function(n){return n = n.split("="),this[n[0]] = n[1],this}.bind({}))[0];
    }

});
$(function() {
    loadPage();
});
$(window).on("popstate", function(){
    loadPage();
});
function loadPage() {
    addListeners();
    repopulateSearchForm();
}
function addListeners() {
    var form_enabled = false;
    $(".search-source-btn").click(function() {
        var $this = $(this);
        $this.css('height', "");
        $this.css('width', "");
        // Disable this button
        $this.prop('disabled', true);
        // Store original height of siblings for re-expansion
        $this.siblings().each(function(){
            $(this).data("height", $(this).css('height'));
            $(this).data("width", $(this).css('width'));
        });
        // Collapse and hide siblings
        $this.siblings().animate(
            {'width': 0, 'height': 0},
            200,
            function(){
                $(this).hide();
                $("#both-button").html("Twitter and Wikipedia");
            }
        );
        // Show the "somewhere else" button
        $("#open-buttons").fadeIn(200).removeClass("hidden");
        // Enable search submit button
        $("#search-submit").prop("disabled", false);
        // Enable search form
        form_enabled = true;
        // Set hidden source input
        $("input[name=source]").val($this.data("choice"));
    });
    $("#open-buttons").click(function(event){
        // Hide this button
        $(this).fadeOut(200);
        // Re-open the search choice buttons
        $("#source-input").children().each(function() {
            var $this = $(this);
            $this.prop("disabled", false);
            $this.show().animate(
                {'width': $this.data('width'), 'height': $this.data('height')},
                200
            );
        });
        $("#both-button").html("both");
        // Disable the search button
        $("#search-submit").prop("disabled", true);
        // Disable the search form
        form_enabled = false;
    });
    $("#search-form").submit(function(event){
        if(form_enabled) {
            newQuerystring = $("#search-form :input[name!='csrfmiddlewaretoken']").serialize();
            history.pushState({}, "", "?"+newQuerystring);
            var $this = $(this);
            event.preventDefault();
            $search_progress = $("#search-progress");
            $search_progress.fadeIn(200).removeClass("hidden");
            $.ajax({
                type: "POST",
                data: $this.serialize(),
                dataType: "json",
                success: function (response) {
                    console.log(response);
                    $search_progress.fadeOut(200);
                    $("#results-container").html(response['reason']);
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(jqXHR);
                    $search_progress.fadeOut(200);
                    $("#results-container").html(jQuery.parseJSON(jqXHR.responseText)['reason']);
                }
            });
        }
    });
}
function repopulateSearchForm() {
    var queryParams = $.getQueryParameters();
    var source = queryParams["source"];
    if (source) {
        $("#"+source+"-button").click();
    }
    var q = queryParams["q"]
    console.log()
    if (q) {
        $("input[name=q]").val(q);
    }
    if (source && q) {
        $("#search-form").submit();
    }
}