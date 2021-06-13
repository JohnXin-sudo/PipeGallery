"use strict";

var id = 370;
var windowsize = 50;
var plotType = "history"; //history,realtime,predict

var plotSpeed = 1.; //秒

var dataTransport = {
  "id": id,
  "windowsize": windowsize,
  "plotType": plotType,
  "plotSpeed": plotSpeed
}; // 基于准备好的dom，初始化echarts实例

var linePh4 = echarts.init(document.querySelector(".linePh4 .chart"));
var lineO2 = echarts.init(document.querySelector(".lineO2 .chart"));
var lineHumility = echarts.init(document.querySelector(".lineHumility .chart"));
var lineTemperature = echarts.init(document.querySelector(".lineTemperature .chart"));
window.addEventListener("resize", function () {
  linePh4.resize();
  lineO2.resize();
  lineHumility.resize();
  lineTemperature.resize();
}); // 打印到python窗口

function print(message) {
  window.pyjs.jsPrint(message);
}

function jsCallback(result) {
  // alert(result)
  // data有四个数据x、 ph4、temperature、humility、o2
  jsonData = JSON.parse(result); // alert(data.temperature)

  var linePh4Option = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器10%
      right: "10%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      } // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]

    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
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
      name: "甲烷",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.ph4
    }]
  };
  var lineO2Option = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器10%
      right: "10%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      } // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]

    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
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
      data: jsonData.o2
    }]
  };
  var lineHumilityOption = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器10%
      right: "10%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      } // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]

    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
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
      name: "湿度",
      type: "line",
      stack: "总量",
      // 是否让线条圆滑显示
      smooth: true,
      data: jsonData.humility
    }]
  };
  var lineTemperatureOption = {
    color: ["#00f2f1", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器10%
      right: "10%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      } // 如果series 里面设置了name，此时图例组件的data可以省略
      // data: ["邮件营销", "联盟广告"]

    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
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
      data: jsonData.temperature
    }]
  };
  linePh4.setOption(linePh4Option);
  lineO2.setOption(lineO2Option);
  lineHumility.setOption(lineHumilityOption);
  lineTemperature.setOption(lineTemperatureOption);
}

function getData() {
  data = JSON.stringify(dataTransport);
  print(data);
  window.pyjs.getData(data, jsCallback); //调用pyqt中的函数进行，将图片传入，异步传回success

  dataTransport.id += 1;
  dataTransport.windowsize = windowsize;
  dataTransport.plotSpeed = plotSpeed; //TODO 这里有bug
}

function historyPlot() {
  dataTransport.plotType = "history";
  stopPlot();
  setInterval(getData, dataTransport.plotSpeed * 1000);
}

function realtimePlot() {
  dataTransport.plotType = "realtime";
  stopPlot();
  setInterval(getData, dataTransport.plotSpeed * 1000);
}

function predictPlot() {
  dataTransport.plotType = "predict";
  stopPlot();
  setInterval(getData, dataTransport.plotSpeed * 1000);
}

function stopPlot() {
  for (var i = 1; i < 100; i++) {
    clearInterval(i); // print(i)
  }
} // python调用js


function pythonCallJs(data) {
  // alert(result)
  // data有四个数据x、 ph4、temperature、humility、o2
  alert(data); // jsonData = JSON.parse(data);
  // alert(data.temperature)
  // var linePh4Option = {
  //   color: ["#00f2f1", "#ed3f35"],
  //   tooltip: {
  //     // 通过坐标轴来触发
  //     trigger: "axis"
  //   },
  //   legend: {
  //     // 距离容器10%
  //     right: "10%",
  //     // 修饰图例文字的颜色
  //     textStyle: {
  //       color: "#4c9bfd"
  //     }
  //     // 如果series 里面设置了name，此时图例组件的data可以省略
  //     // data: ["邮件营销", "联盟广告"]
  //   },
  //   grid: {
  //     top: "20%",
  //     left: "3%",
  //     right: "4%",
  //     bottom: "3%",
  //     show: true,
  //     borderColor: "#012f4a",
  //     containLabel: true
  //   },
  //   xAxis: {
  //     type: "category",
  //     boundaryGap: false,
  //     data: jsonData.x,
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 去除x坐标轴的颜色
  //     axisLine: {
  //       show: false
  //     }
  //   },
  //   yAxis: {
  //     type: "value",
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 修改y轴分割线的颜色
  //     splitLine: {
  //       lineStyle: {
  //         color: "#012f4a"
  //       }
  //     }
  //   },
  //   series: [{
  //     name: "甲烷",
  //     type: "line",
  //     stack: "总量",
  //     // 是否让线条圆滑显示
  //     smooth: true,
  //     data: jsonData.ph4
  //   }]
  // };
  // var lineO2Option = {
  //   color: ["#00f2f1", "#ed3f35"],
  //   tooltip: {
  //     // 通过坐标轴来触发
  //     trigger: "axis"
  //   },
  //   legend: {
  //     // 距离容器10%
  //     right: "10%",
  //     // 修饰图例文字的颜色
  //     textStyle: {
  //       color: "#4c9bfd"
  //     }
  //     // 如果series 里面设置了name，此时图例组件的data可以省略
  //     // data: ["邮件营销", "联盟广告"]
  //   },
  //   grid: {
  //     top: "20%",
  //     left: "3%",
  //     right: "4%",
  //     bottom: "3%",
  //     show: true,
  //     borderColor: "#012f4a",
  //     containLabel: true
  //   },
  //   xAxis: {
  //     type: "category",
  //     boundaryGap: false,
  //     data: jsonData.x,
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 去除x坐标轴的颜色
  //     axisLine: {
  //       show: false
  //     }
  //   },
  //   yAxis: {
  //     type: "value",
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 修改y轴分割线的颜色
  //     splitLine: {
  //       lineStyle: {
  //         color: "#012f4a"
  //       }
  //     }
  //   },
  //   series: [{
  //     name: "氧气",
  //     type: "line",
  //     stack: "总量",
  //     // 是否让线条圆滑显示
  //     smooth: true,
  //     data: jsonData.O2
  //   }]
  // };
  // var lineHumilityOption = {
  //   color: ["#00f2f1", "#ed3f35"],
  //   tooltip: {
  //     // 通过坐标轴来触发
  //     trigger: "axis"
  //   },
  //   legend: {
  //     // 距离容器10%
  //     right: "10%",
  //     // 修饰图例文字的颜色
  //     textStyle: {
  //       color: "#4c9bfd"
  //     }
  //     // 如果series 里面设置了name，此时图例组件的data可以省略
  //     // data: ["邮件营销", "联盟广告"]
  //   },
  //   grid: {
  //     top: "20%",
  //     left: "3%",
  //     right: "4%",
  //     bottom: "3%",
  //     show: true,
  //     borderColor: "#012f4a",
  //     containLabel: true
  //   },
  //   xAxis: {
  //     type: "category",
  //     boundaryGap: false,
  //     data: jsonData.x,
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 去除x坐标轴的颜色
  //     axisLine: {
  //       show: false
  //     }
  //   },
  //   yAxis: {
  //     type: "value",
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 修改y轴分割线的颜色
  //     splitLine: {
  //       lineStyle: {
  //         color: "#012f4a"
  //       }
  //     }
  //   },
  //   series: [{
  //     name: "湿度",
  //     type: "line",
  //     stack: "总量",
  //     // 是否让线条圆滑显示
  //     smooth: true,
  //     data: jsonData.humility
  //   }]
  // };
  // var lineTemperatureOption = {
  //   color: ["#00f2f1", "#ed3f35"],
  //   tooltip: {
  //     // 通过坐标轴来触发
  //     trigger: "axis"
  //   },
  //   legend: {
  //     // 距离容器10%
  //     right: "10%",
  //     // 修饰图例文字的颜色
  //     textStyle: {
  //       color: "#4c9bfd"
  //     }
  //     // 如果series 里面设置了name，此时图例组件的data可以省略
  //     // data: ["邮件营销", "联盟广告"]
  //   },
  //   grid: {
  //     top: "20%",
  //     left: "3%",
  //     right: "4%",
  //     bottom: "3%",
  //     show: true,
  //     borderColor: "#012f4a",
  //     containLabel: true
  //   },
  //   xAxis: {
  //     type: "category",
  //     boundaryGap: false,
  //     data: jsonData.x,
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 去除x坐标轴的颜色
  //     axisLine: {
  //       show: false
  //     }
  //   },
  //   yAxis: {
  //     type: "value",
  //     // 去除刻度
  //     axisTick: {
  //       show: false
  //     },
  //     // 修饰刻度标签的颜色
  //     axisLabel: {
  //       color: "rgba(255,255,255,.7)"
  //     },
  //     // 修改y轴分割线的颜色
  //     splitLine: {
  //       lineStyle: {
  //         color: "#012f4a"
  //       }
  //     }
  //   },
  //   series: [{
  //     name: "温度",
  //     type: "line",
  //     stack: "总量",
  //     // 是否让线条圆滑显示
  //     smooth: true,
  //     data: jsonData.temperature
  //   }]
  // };
  // linePh4.setOption(linePh4Option);
  // lineO2.setOption(lineO2Option);
  // lineHumility.setOption(lineHumilityOption);
  // lineTemperature.setOption(lineTemperatureOption);

  return "success";
} // button clicked


function plotId() {
  document.getElementById("ID").innerText;
  dataTransport.id = document.getElementById("ID").innerText = "";
}

function plotNum() {
  dataTransport.windowsize = document.getElementById("num").innerText;
}

function plotSp() {
  dataTransport.plotSpeed = document.getElementById("speed").innerText;
}