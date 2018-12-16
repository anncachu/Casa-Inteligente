$(function () {
    $(".hab button").on('click', function () {
        Project.Focos.turnOnLed($(this).data('id'));
    });
});