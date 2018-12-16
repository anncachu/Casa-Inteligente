$(function () {
    $(".hab button").on('click', function () {
        const id = $(this).data('id');
        const script = `frame1foco${id}.php`;
        Project.request(`focos/${script}`).done(data => {
            console.log(data);
            Project.toast({message: `Foco ${id} encendido`, type: 'success', duration: 2000});
        });
    })
});