const eventEmitter = require('events');

class MyEmitter extends eventEmitter {}

// init obj
const myEmit = new MyEmitter();

//Event emitter
myEmit.on('event', ()=> console.log('Event Fired'));

//init event
myEmit.emit('event');