
agro.controller('controllerHome',function($scope,$log,$http,$state){


    $scope.irrigationError = true;


    //api call for irrigation
    $scope.getIrrigation = function(){

      console.log("------irrigation------");
      console.log($scope.countyname);
      console.log($scope.typeofplant);

        $http({
    			method : "POST",
    			url : '/modal1',
          data: {
            countyname: $scope.countyname,
            typeofplant: $scope.typeofplant
          }
    		}).success(function(data) {

            console.log("-----irrigation-----");
            console.log(data);

    		}).error(function(error) {
    			console.log("Internal Server error occurred");
          $scope.irrigationError = true;
    		});

    };


    //api call for irrigation
    $scope.getCropYield = function(){

        $http({
          method : "POST",
          url : '/modal2',
          data: {
            countyname: $scope.countyname,
            area: $scope.area
          }
        }).success(function(data) {



        }).error(function(error) {
          console.log("Internal Server error occurred");
          $scope.irrigationError = true;
        });

    };

})
