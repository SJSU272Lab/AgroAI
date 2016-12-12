
agro.controller('controllerHome',function($scope,$log,$http,$state){


    $scope.irrigationError = false;
    $scope.cropYieldError = false;
    $scope.cropNonIrrigatedError = false;
    $scope.soilErrosionPreventionError = false;
    $scope.successMsg = false;
    $scope.submitDataError = false;

    $scope.yieldUnit = null;


    //
    // $scope.cropAreaChanged = function(){
    //   console.log("changed");
    //    if($scope.area == "Other"){
    //         $('html #areaCrop').after("<label class='form-control'>Enter your area<input class='form-control' placeholder='Enter your area' ng-model='area'></input></label>");
    //    }
    //    else{
    //         $('label').remove();
    //    }
    //
    // };


    $scope.irrigationFocus = function() {
        console.log("irrigationFocus");
        var element = document.getElementById('irrigation');
        if(element)
          element.focus();
    };


    //api call for irrigation
    $scope.getIrrigation = function(){

      console.log("------irrigation------");
      console.log($scope.countyname);
      console.log($scope.typeofplant);

        $http({
    			method : "POST",
    			url : '/model1',
          data: {
            countyname: $scope.countyname,
            typeofplant: $scope.typeofplant
          }
    		}).success(function(data) {

            console.log("-----irrigation-----");
            console.log(data);


            console.log("inside function");
            Highcharts.chart('modelIrrigation', {
                chart: {
                    type: 'column',
                    options3d: {
                         enabled: true,
                         alpha: 15,
                         beta: 15,
                         depth: 50,
                         viewDistance: 25
                     }
                },
                colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572',
                          '#FF9655', '#FFF263', '#6AF9C4'],
                title: {
                    text: 'Irrigation for the Year ahead'
                },
                xAxis: {
                    type: 'category',
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Water per square feet (gallons)'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: 'Irrigation for the Year ahead<b>{point.y:.3f} gallons</b>'
                },
                series: [{
                    name: 'Irrigation',
                    data: [
                        ['January', data.Jan],
                        ['February', data.Feb],
                        ['March', data.Mar],
                        ['April', data.Apr],
                        ['May', data.May],
                        ['June', data.Jun],
                        ['July', data.Jul],
                        ['August', data.Aug],
                        ['Sept', data.Sep],
                        ['October', data.Oct],
                        ['November', data.Nov],
                        ['December', data.Dec]
                    ],
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
                        format: '{point.y:.3f}', // one decimal
                        y: 10, // 10 pixels down from the top
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                }]
            });

            //appyl the theme
            Highcharts.setOptions(Highcharts.theme);


    		}).error(function(error) {
    			console.log("Internal Server error occurred");
          $scope.irrigationError = true;
    		});

    };


    //api call for irrigation
    $scope.getCropYield = function(){

        $http({
          method : "POST",
          url : '/model2',
          data: {
            countyname: $scope.countynameForCrop,
            area: $scope.area
          }
        }).success(function(data) {

          console.log("-----getCropYield-----");
          console.log(data);
          console.log(Object.keys(data));
          console.log(Object.values(data));

          var keys = Object.keys(data),
              values = Object.values(data);



          Highcharts.chart('modelCropYeild', {
              chart: {
                  type: 'column'
              },
              colors: ['#f45b5b', '#8085e9', '#8d4654', '#7798BF', '#aaeeee', '#ff0066', '#eeaaee',
                        '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
              title: {
                  text: 'Crop suggestion for your soil type'
              },
              plotOptions: {
                  column: {
                      depth: 25
                  }
              },
              xAxis: {
                  type: 'category',
                  labels: {
                      rotation: -45,
                      style: {
                          fontSize: '13px',
                          fontFamily: 'Verdana, sans-serif'
                      }
                  }
              },
              yAxis: {
                  min: 0,
                  title: {
                      text: 'Crop Yield (tons/crates)'
                  }
              },
              legend: {
                  enabled: false
              },
              tooltip: {
                  pointFormat: 'Crop suggestion for your soil type'
              },
              series: [{
                  name: 'Crop yield',
                  data: [
                      [keys[0], values[0]],
                      [keys[1], values[1]],
                      [keys[2], values[2]],
                      [keys[3], values[3]],
                      [keys[4], values[4]]
                  ]
              }],
              dataLabels: {
                  enabled: true,
                  rotation: -90,
                  color: '#FFFFFF',
                  align: 'right',
                  format: '{point.y:.3f}', // one decimal
                  y: 10, // 10 pixels down from the top
                  style: {
                      fontSize: '13px',
                      fontFamily: 'Verdana, sans-serif'
                  }
              }
          });

          //appyl the theme
          Highcharts.setOptions(Highcharts.theme);


        }).error(function(error) {
          console.log("Internal Server error occurred");
          $scope.cropYieldError = true;
        });

    };


    //api call for irrigation
    $scope.cropNonIrrigated = function(){

        $http({
          method : "POST",
          url : '/model3',
          data: {
            countyname: $scope.countynameForCropNonIrrigation,
            area: $scope.areaForCropNonIrrigation
          }
        }).success(function(data) {

          console.log("-----cropNonIrrigated-----");
          console.log(data);
          console.log(Object.keys(data));
          console.log(Object.values(data));

          var keys = Object.keys(data),
              values = Object.values(data);



          Highcharts.chart('modelCropYeildNonIrrigation', {
              chart: {
                  type: 'column',
                  options3d: {
                       enabled: true,
                       alpha: 15,
                       beta: 15,
                       depth: 50,
                       viewDistance: 25
                   }
              },
              title: {
                  text: 'Crop suggestion for your soil type - Non Irrigated mode'
              },
              plotOptions: {
                  column: {
                      depth: 25
                  }
              },
              xAxis: {
                  type: 'category',
                  labels: {
                      rotation: -45,
                      style: {
                          fontSize: '13px',
                          fontFamily: 'Verdana, sans-serif'
                      }
                  }
              },
              yAxis: {
                  min: 0,
                  title: {
                      text: 'Crop Yield (tons/crates)'
                  }
              },
              legend: {
                  enabled: false
              },
              tooltip: {
                  pointFormat: 'Crop suggestion for your soil type - Non Irrigated mode'
              },
              series: [{
                  name: 'Crop yield - Non Irrigated mode',
                  data: [
                      [keys[0], values[0]],
                      [keys[1], values[1]],
                      [keys[2], values[2]],
                      [keys[3], values[3]],
                      [keys[4], values[4]]
                  ]
              }],
              dataLabels: {
                  enabled: true,
                  rotation: -90,
                  color: '#FFFFFF',
                  align: 'right',
                  format: '{point.y:.3f}', // one decimal
                  y: 10, // 10 pixels down from the top
                  style: {
                      fontSize: '13px',
                      fontFamily: 'Verdana, sans-serif'
                  }
              }
          });




        }).error(function(error) {
          console.log("Internal Server error occurred");
          $scope.cropNonIrrigatedError = true;
        });

    };


    //api call for irrigation
    $scope.soilErrosionPrevention = function(){

        $http({
          method : "POST",
          url : '/model4',
          data: {
            countyname: $scope.countynameForSoilPrevention
          }
        }).success(function(data) {

          console.log("-----soilErrosionPrevention-----");
          console.log(data);
          console.log(Object.keys(data));
          console.log(Object.values(data));

          var keys = Object.keys(data),
              values = Object.values(data);



          Highcharts.chart('modelSoilErosion', {
              chart: {
                  type: 'column',
                  options3d: {
                       enabled: true,
                       alpha: 15,
                       beta: 15,
                       depth: 50,
                       viewDistance: 25
                   }
              },
              colors: ['#7cb5ec', '#f7a35c', '#90ee7e', '#7798BF', '#aaeeee', '#ff0066', '#eeaaee',
                        '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
              title: {
                  text: 'Soil erosion prevention by Planting trees'
              },
              plotOptions: {
                  column: {
                      depth: 25
                  }
              },
              xAxis: {
                  type: 'category',
                  labels: {
                      rotation: -45,
                      style: {
                          fontSize: '13px',
                          fontFamily: 'Verdana, sans-serif'
                      }
                  }
              },
              yAxis: {
                  min: 0,
                  title: {
                      text: 'Optimal height of the tree (feet)'
                  }
              },
              legend: {
                  enabled: false
              },
              tooltip: {
                  pointFormat: 'Soil erosion prevention by Planting trees'
              },
              series: [{
                  name: 'Trees',
                  data: [
                      [keys[0], values[0]],
                      [keys[1], values[1]],
                      [keys[2], values[2]],
                      [keys[3], values[3]],
                      [keys[4], values[4]]
                  ]
              }],
              dataLabels: {
                  enabled: true,
                  rotation: -90,
                  color: '#FFFFFF',
                  align: 'right',
                  format: '{point.y:.3f}', // one decimal
                  y: 10, // 10 pixels down from the top
                  style: {
                      fontSize: '13px',
                      fontFamily: 'Verdana, sans-serif'
                  }
              }
          });


          //appyl the theme
          Highcharts.setOptions(Highcharts.theme);

        }).error(function(error) {
          console.log("Internal Server error occurred");
          $scope.soilErrosionPreventionError = true;
        });

    };

    //api call for submitData
    $scope.submitData = function(){

        console.log("-----------submitData---------");
        console.log($scope.state,
                    $scope.county,
                    $scope.crop,
                    $scope.yield,
                    $scope.yieldUnit,
                    $scope.irrigation,
                    $scope.irrigationArea,
                    $scope.irrigationFrequency
                  );

	    var captchaResponse = grecaptcha.getResponse();
	    if(captchaResponse != "" && captchaResponse != undefined && captchaResponse != null)
        {
            $http({
			    method : "POST",
			    url : 'https://www.google.com/recaptcha/api/siteverify',
			    data : {
				    "secret" : "6LcRjQ4UAAAAAI0AssSLOG_ee9tZeLMO6rVA-CBc",
                    "response" : captchaResponse

			    }
            }).success(function(data) {

                if(data.success == true) {
                    $http({
                        method: "POST",
                        url: '/userdata',
                        data: {
                            state: $scope.state,
                            county: $scope.county,
                            crop: $scope.crop,
                            yield: $scope.yield,
                            yieldUnit: $scope.yieldUnit,
                            irrigation: $scope.irrigation,
                            irrigationArea: $scope.irrigationArea,
                            irrigationFrequency: $scope.irrigationFrequency
                        }
                    }).success(function (data) {

                        console.log("-----soilErrosionPrevention-----");
                        console.log(data);

                        if (data) {
                            $scope.successMsg = true;
                            $scope.state = "",
                            $scope.county = "",,
                            $scope.crop = "",
                            $scope.yield = "",
                            $scope.yieldUnit = "",
                            $scope.irrigation  = "",
                            $scope.irrigationArea = "",
                            $scope.irrigationFrequency = "";
                            alert("Thank you for your input. Your data is submitted successfully");
                          }
                        else
                            alert("Thank you for your input. Your data is submitted successfully");


                    }).error(function (error) {
                        console.log("Internal Server error occurred");
                        $scope.submitDataError = true;
                    });
                }else{

                }

                console.log(data.success);
    		}).error(function(error) {
			    console.log("Error")

		    });

        }










    };


    // $scope.submit = function() {
    //
	 //    var captchaResponse = grecaptcha.getResponse();
	 //    if(captchaResponse != "" && captchaResponse != undefined && captchaResponse != null)
    //     {
    //         $http({
		// 	    method : "POST",
		// 	    url : 'https://www.google.com/recaptcha/api/siteverify',
		// 	    data : {
		// 		    "secret" : "6LcRjQ4UAAAAAI0AssSLOG_ee9tZeLMO6rVA-CBc",
    //                 "response" : captchaResponse
    //
		// 	    }
    //         }).success(function(data) {
    //             console.log(data.success);
    // 		}).error(function(error) {
		// 	    console.log("Error")
    //
		//     });
    //
    //     }
    // }




})
