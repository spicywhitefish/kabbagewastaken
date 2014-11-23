$(function(){
    $(".search-source-btn").click(function() {
        var $this = $(this);
        // Store original height of siblings for re-expansion
        $this.siblings().each(function(){
            $(this).data("height", $(this).css('height'));
            $(this).data("width", $(this).css('width'));
        });
        // Collapse and hide siblings
        $this.siblings().animate(
            {'width': 0, 'height': 0},
            200,
            function(){$(this).hide()}
        );
        // Show the "somewhere else" button
        $("#open-buttons").fadeIn(200).removeClass("hidden");
    });
    $("#open-buttons").click(function(event){
        // Hide this button
        $(this).fadeOut(200);
        // Re-open the search choice buttons
        $("#source-input").children().each(function() {
            var $this = $(this);
            $this.show().animate(
                {'width': $this.data('width'), 'height': $this.data('height')},
                200
            );
        });
    });
});