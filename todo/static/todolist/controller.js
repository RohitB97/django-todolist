/*var app = angular.module("home",[]);

app.controller("homeCtrl",function($scope){
       $scope.task = {name:'nigga'};
});*/

function addtask(){
    $('#task_form').submit();	
};

function clearfield(){
	$('#task_input').val('');
};