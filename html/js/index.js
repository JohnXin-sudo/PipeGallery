
var id = 371;
var windowsize = 50;
var plotType = "history"; //history,realtime,predict
var plotSpeed = 1.; //秒

var dataTransport = {
  "id": id,
  "windowsize": windowsize,
  "plotType": plotType,
  "plotSpeed": plotSpeed
}

// 基于准备好的dom，初始化echarts实例
var linePh4 = echarts.init(document.querySelector(".linePh4 .chart"));
var lineO2 = echarts.init(document.querySelector(".lineO2 .chart"));
var lineHumility = echarts.init(document.querySelector(".lineHumility .chart"));
var lineTemperature = echarts.init(document.querySelector(".lineTemperature .chart"));

window.addEventListener("resize", function () {
  linePh4.resize();
  lineO2.resize();
  lineHumility.resize();
  lineTemperature.resize();
});

$

// 打印到python窗口
function print(message) {
  window.pyjs.jsPrint(message)
}

function jsCallback(result) {
  // alert(result)
  // data有四个数据x、 ph4、temperature、humility、o2
  jsonData = JSON.parse(result);
  // alert(data.temperature)
  var linePh4Option = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器5%
      right: "5%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      },
      icon: 'roundRect', //icon为圆角矩形
      // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]
    },
    grid: {
      top: "10%",
      left: "2%",
      right: "2%",
      bottom: "5%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: jsonData.x,
      // 去除刻度
      axisTick: {
        show: true
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 去除x坐标轴的颜色
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      // 去除刻度
      axisTick: {
        show: false
      },
      min:-2,
      max:20,
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 修改y轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [{
      name: "甲烷",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.ph4,
      color: "red",
      itemStyle: {
        color: '#6A5ACD',
        normal: {
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'solid',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#0000FF'
            }, {
              offset: 1,
              color: '#CD5C5C'
            }]), //线条渐变色  
          }
        },
        emphasis: {
          color: '#6A5ACD',
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'dotted',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#1E90FF'
            }, {
              offset: 1,
              color: '#0000FF'
            }])
          }
        }
      }, //线条样式 
      areaStyle: {
        normal: {
          //颜色渐变函数 前四个参数分别表示四个位置依次为左、下、右、上
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{

            offset: 0,
            color: 'rgba(80,141,255,0.39)'
          }, {
            offset: .34,
            color: 'rgba(56,155,255,0.25)'
          }, {
            offset: 1,
            color: 'rgba(38,197,254,0.00)'
          }])

        }
      }, //区域颜色渐变

    }, ]

  };

  var lineO2Option = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器5%
      right: "5%",
      // 修饰图例文字的颜色
      icon: 'roundRect', //icon为圆角矩形
      textStyle: {
        color: "#4c9bfd"
      }
      // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]
    },
    grid: {
      top: "10%",
      left: "2%",
      right: "2%",
      bottom: "5%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: jsonData.x,
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 去除x坐标轴的颜色
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 修改y轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [{
      name: "氧气",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.o2,
      color: "green",

      itemStyle: {
        color: '#6A5ACD',
        normal: {
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'solid',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#0000FF'
            }, {
              offset: 1,
              color: '#CD5C5C'
            }]), //线条渐变色  
          }
        },
        emphasis: {
          color: '#6A5ACD',
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'dotted',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#1E90FF'
            }, {
              offset: 1,
              color: '#0000FF'
            }])
          }
        }
      }, //线条样式 
      areaStyle: {
        normal: {
          //颜色渐变函数 前四个参数分别表示四个位置依次为左、下、右、上
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{

            offset: 0,
            color: 'rgba(80,141,255,0.39)'
          }, {
            offset: .34,
            color: 'rgba(56,155,255,0.25)'
          }, {
            offset: 1,
            color: 'rgba(38,197,254,0.00)'
          }])

        }
      }, //区域颜色渐变
    }, ]

  };
  var lineHumilityOption = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器5%
      right: "5%",
      icon: 'roundRect', //icon为圆角矩形
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      }
      // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]
    },
    grid: {
      top: "10%",
      left: "2%",
      right: "2%",
      bottom: "5%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: jsonData.x,
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 去除x坐标轴的颜色
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      // 去除刻度
      axisTick: {
        show: false
      },
      min: 60,
      max:100,
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 修改y轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [{
      name: "湿度",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.humility,
      color: "blue",
      itemStyle: {
        color: '#6A5ACD',
        normal: {
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'solid',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#0000FF'
            }, {
              offset: 1,
              color: '#CD5C5C'
            }]), //线条渐变色  
          }
        },
        emphasis: {
          color: '#6A5ACD',
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'dotted',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#1E90FF'
            }, {
              offset: 1,
              color: '#0000FF'
            }])
          }
        }
      }, //线条样式 
      areaStyle: {
        normal: {
          //颜色渐变函数 前四个参数分别表示四个位置依次为左、下、右、上
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{

            offset: 0,
            color: 'rgba(80,141,255,0.39)'
          }, {
            offset: .34,
            color: 'rgba(56,155,255,0.25)'
          }, {
            offset: 1,
            color: 'rgba(38,197,254,0.00)'
          }])

        }
      }, //区域颜色渐变
    }]

  };
  var lineTemperatureOption = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器5%
      right: "5%",
      icon: 'roundRect', //icon为圆角矩形
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      }
      // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]
    },
    grid: {
      top: "10%",
      left: "2%",
      right: "2%",
      bottom: "5%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      data: jsonData.x,
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 去除x坐标轴的颜色
      axisLine: {
        show: false
      }
    },
    yAxis: {
      type: "value",
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 修改y轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [{
      name: "温度",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.temperature,
      color: "yellow",
      itemStyle: {
        color: '#6A5ACD',
        normal: {
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'solid',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#0000FF'
            }, {
              offset: 1,
              color: '#CD5C5C'
            }]), //线条渐变色  
          }
        },
        emphasis: {
          color: '#6A5ACD',
          lineStyle: { // 系列级个性化折线样式  
            width: 2,
            type: 'dotted',
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 0,
              color: '#1E90FF'
            }, {
              offset: 1,
              color: '#0000FF'
            }])
          }
        }
      }, //线条样式 
      areaStyle: {
        normal: {
          //颜色渐变函数 前四个参数分别表示四个位置依次为左、下、右、上
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{

            offset: 0,
            color: 'rgba(80,141,255,0.39)'
          }, {
            offset: .34,
            color: 'rgba(56,155,255,0.25)'
          }, {
            offset: 1,
            color: 'rgba(38,197,254,0.00)'
          }])

        }
      }, //区域颜色渐变

    }, ]

  };


  linePh4.setOption(linePh4Option);
  lineO2.setOption(lineO2Option);
  lineHumility.setOption(lineHumilityOption);
  lineTemperature.setOption(lineTemperatureOption);


}

function getData() {
  data = JSON.stringify(dataTransport);
  print(data)
  window.pyjs.getData(data, jsCallback); //调用pyqt中的函数进行，将图片传入，异步传回success
  dataTransport.id += 1;
  dataTransport.windowsize = windowsize;
  dataTransport.plotSpeed = plotSpeed //TODO 这里有bug
}
// jQuery.support.cors = true;
function historyPlot() {
  stopPlot()
  plotType = "history";
  t = setInterval(function(){
    $.ajax({
      url: "http://127.0.0.1:8000/data/?id="+id+"&windowsize="+
                                             windowsize + 
                                             "&plotType="+plotType+
                                             "&plotSpeed="+plotSpeed,
      // data:JSON.stringify(dataTransport),
      datatype: "json",
      type: "GET",
      success: function (result){
        speed = plotSpeed
        
        id+=1,
        jsCallback(result)
        // t = setTimeout(time, plotSpeed * 1000); //设定定时器，循环运行
      },
      error: function (e) {
      } 
    })
  }
    , plotSpeed * 1000); //開始运行
  
}

function realtimePlot() {
  stopPlot()
  plotType = "realtime";
  t = setInterval(function(){
    $.ajax({
      url: "http://127.0.0.1:8000/data/?id="+id+"&windowsize="+
                                             windowsize + 
                                             "&plotType="+plotType+
                                             "&plotSpeed="+plotSpeed,
      // data:JSON.stringify(dataTransport),
      datatype: "json",
      type: "GET",
      success: function (result){
        speed = plotSpeed
        
        // id+=1,
        jsCallback(result)
        // t = setTimeout(time, plotSpeed * 1000); //设定定时器，循环运行
      },
      error: function (e) {
      } 
    })
  }
    , plotSpeed * 1000); //開始运行
}

function predictPlot() {
  stopPlot()
  plotType = "predict";
  t = setInterval(function(){
    $.ajax({
      url: "http://127.0.0.1:8000/data/?id="+id+"&windowsize="+
                                             windowsize + 
                                             "&plotType="+plotType+
                                             "&plotSpeed="+plotSpeed,
      // data:JSON.stringify(dataTransport),
      datatype: "json",
      type: "GET",
      success: function (result){
        speed = plotSpeed
        
        id+=1,
        jsCallback(result)
        // t = setTimeout(time, plotSpeed * 1000); //设定定时器，循环运行
      },
      error: function (e) {
      } 
    })
  }
    , plotSpeed * 1000); //開始运行
}

function stopPlot() {
  for (var i = 1; i < 100; i++) {
    clearInterval(i);
  }
}

// python调用js
function pythonCallJs(data) {
  // alert(result)
  // data有四个数据x、 ph4、temperature、humility、o2
  alert(data)
  return "success"
}


// button clicked

function isEmpty(obj) {
  if (typeof obj == "undefined" || obj == null || obj == "") {
    return true;
  } else {
    return false;
  }
}

function plotId() {
  str = document.getElementById("ID").value;
  // print(str)
  if (isEmpty(str)) {
    print("输入数据为空" + str)
    return false;
  }
  if (id = parseInt(str)) {} else {
    print("输入数据错误" + str)
  }
  document.getElementById("ID").value="";
}

function plotNum() {
  str = document.getElementById("num").value;

  if (isEmpty(str)) {
    print("输入数据为空" + str)
    return false;
  }
  if (windowsize = parseInt(str)) {} else {
    print("输入数据错误" + str)
  }
  document.getElementById("num").value="";
}

function plotSp() {
  str = document.getElementById("speed").value;
  print(str)
  if (isEmpty(str)) {
    print("输入数据为空" + str)
    return false;
  }
  if (plotSpeed = parseInt(str)) {

  } else {
    print("输入数据错误" + str)
    return false
  }
  document.getElementById("speed").value="";
}