Project = require('./init.js');
Project.Focos = {
    turnOnLed: function (id) {
        const script = `frame1foco${id}.php`;
        Project.request(`focos/${script}`).done(data => {
            console.log(data);
            Project.toast({message: `Foco ${id} encendido`, type: 'success', duration: 2000});
        });
    }
};