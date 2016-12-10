var agro = angular.module('Agro',['ui.router']);
//handles client side routing
console.log("here");
console.log(agro);
agro.config(function($stateProvider, $urlRouterProvider){

	$urlRouterProvider.
		otherwise('/');

	$stateProvider
		.state('home',
			{
				url:'/',
        templateUrl : '/home',
				controller : 'controllerHome',
			})


})
