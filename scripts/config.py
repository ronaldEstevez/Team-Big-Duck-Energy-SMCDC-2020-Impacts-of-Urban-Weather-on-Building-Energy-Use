dailyAvgTemp = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "month"
                  ],
                  "id": "hzkmcsk8",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1422511408000,
                      1422596342000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "avg(temp_K)",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "ekb8nad",
                    "type": "point",
                    "config": {
                        "dataId": "month",
                        "label": "Point",
                        "color": [
                          18,
                          147,
                          154
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 10,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#FFC300",
                                    "#F1920E",
                                    "#E3611C",
                                    "#C70039",
                                    "#900C3F",
                                    "#5A1846"
                                ],
                                "reversed": True
                            },
                            "strokeColorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#5A1846",
                                    "#900C3F",
                                    "#C70039",
                                    "#E3611C",
                                    "#F1920E",
                                    "#FFC300"
                                ]
                            },
                            "radiusRange": [
                                0,
                                50
                            ],
                            "filled": True
                        },
                        "hidden": False,
                        "textLabel": []
                    },
                    "visualChannels": {
                        "colorField": {
                            "name": "avg(temp_K)",
                            "type": "real"
                        },
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": {
                            "name": "avg(temp_K)",
                            "type": "real"
                        },
                        "sizeScale": "sqrt"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "month": [
                            "time",
                            "avg(temp_K)"
                        ]
                    },
                    "enabled": True
                },
                "brush": {
                    "size": 0.5,
                    "enabled": False
                },
                "geocoder": {
                    "enabled": False
                },
                "coordinate": {
                    "enabled": False
                }
            },
            "layerBlending": "normal",
            "splitMaps": [],
            "animationConfig": {
                "currentTime": None,
                "speed": 1
            }
        },
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 41.87023601152249,
            "longitude": -87.62864207899815,
            "pitch": 0,
            "zoom": 12.183388142618051,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "dark",
            "topLayerGroups": {},
            "visibleLayerGroups": {
                "label": True,
                "road": True,
                "border": False,
                "building": True,
                "water": True,
                "land": True,
                "3d building": False
            },
            "threeDBuildingColor": [
                9.665468314072013,
                17.18305478057247,
                31.1442867897876
            ],
            "mapStyles": {}
        }
    }
}

dailyAvgWindSpeed = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "month"
                  ],
                  "id": "nmadvrb4",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1430438400000,
                      1430523955000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "avg(`WindSpd_ms-1`)",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "bfil4c",
                    "type": "point",
                    "config": {
                        "dataId": "month",
                        "label": "Point",
                        "color": [
                          218,
                          112,
                          191
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 10,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#FFC300",
                                    "#F1920E",
                                    "#E3611C",
                                    "#C70039",
                                    "#900C3F",
                                    "#5A1846"
                                ],
                                "reversed": True
                            },
                            "strokeColorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#5A1846",
                                    "#900C3F",
                                    "#C70039",
                                    "#E3611C",
                                    "#F1920E",
                                    "#FFC300"
                                ]
                            },
                            "radiusRange": [
                                0,
                                50
                            ],
                            "filled": True
                        },
                        "hidden": False,
                        "textLabel": [
                            {
                                "field": None,
                                "color": [
                                    255,
                                    255,
                                    255
                                ],
                                "size": 18,
                                "offset": [
                                    0,
                                    0
                                ],
                                "anchor": "start",
                                "alignment": "center"
                            }
                        ]
                    },
                    "visualChannels": {
                        "colorField": {
                            "name": "avg(`WindSpd_ms-1`)",
                            "type": "real"
                        },
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": {
                            "name": "avg(`WindSpd_ms-1`)",
                            "type": "real"
                        },
                        "sizeScale": "sqrt"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "month": [
                            "time",
                            "avg(`WindSpd_ms-1`)"
                        ]
                    },
                    "enabled": True
                },
                "brush": {
                    "size": 0.5,
                    "enabled": False
                },
                "geocoder": {
                    "enabled": False
                },
                "coordinate": {
                    "enabled": False
                }
            },
            "layerBlending": "normal",
            "splitMaps": [],
            "animationConfig": {
                "currentTime": None,
                "speed": 1
            }
        },
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 41.86603772017152,
            "longitude": -87.6355647670081,
            "pitch": 0,
            "zoom": 11.905345338119592,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "dark",
            "topLayerGroups": {},
            "visibleLayerGroups": {
                "label": True,
                "road": True,
                "border": False,
                "building": True,
                "water": True,
                "land": True,
                "3d building": False
            },
            "threeDBuildingColor": [
                9.665468314072013,
                17.18305478057247,
                31.1442867897876
            ],
            "mapStyles": {}
        }
    }
}

dailyTemp = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
                {
                    "dataId": [
                        "day"
                    ],
                    "id": "fja631mn9",
                    "name": [
                        "time"
                    ],
                    "type": "timeRange",
                    "value": [
                        1445282910000,
                        1445283839000
                    ],
                    "enlarged": True,
                    "plotType": "lineChart",
                    "yAxis": {
                        "name": "temp_K",
                        "type": "real"
                    }
                }
            ],
            "layers": [
                {
                    "id": "muwb0v",
                    "type": "point",
                    "config": {
                        "dataId": "day",
                        "label": "Point",
                        "color": [
                          136,
                          87,
                          44
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 10,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "Global Warming 8",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#FFC300",
                                    "#E57F00",
                                    "#CB4600",
                                    "#B21800",
                                    "#98000A",
                                    "#7F0023",
                                    "#650031",
                                    "#4C0035"
                                ],
                                "reversed": True
                            },
                            "strokeColorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#5A1846",
                                    "#900C3F",
                                    "#C70039",
                                    "#E3611C",
                                    "#F1920E",
                                    "#FFC300"
                                ]
                            },
                            "radiusRange": [
                                1,
                                50
                            ],
                            "filled": True
                        },
                        "hidden": False,
                        "textLabel": []
                    },
                    "visualChannels": {
                        "colorField": {
                            "name": "temp_K",
                            "type": "real"
                        },
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": {
                            "name": "temp_K",
                            "type": "real"
                        },
                        "sizeScale": "sqrt"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "day": [
                            "time",
                            "temp_K"
                        ]
                    },
                    "enabled": True
                },
                "brush": {
                    "size": 0.5,
                    "enabled": False
                },
                "geocoder": {
                    "enabled": False
                },
                "coordinate": {
                    "enabled": False
                }
            },
            "layerBlending": "normal",
            "splitMaps": [],
            "animationConfig": {
                "currentTime": None,
                "speed": 1
            }
        },
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 41.87348965518838,
            "longitude": -87.62208596192067,
            "pitch": 0,
            "zoom": 12.903882166166095,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "dark",
            "topLayerGroups": {},
            "visibleLayerGroups": {
                "label": True,
                "road": True,
                "border": False,
                "building": True,
                "water": True,
                "land": True,
                "3d building": False
            },
            "threeDBuildingColor": [
                9.665468314072013,
                17.18305478057247,
                31.1442867897876
            ],
            "mapStyles": {}
        }
    }
}

dailyWindSpeed = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "day"
                  ],
                  "id": "xmowh9a9w",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1433116800000,
                      1433117729000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "WindSpd_ms-1",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "kzaeypq",
                    "type": "point",
                    "config": {
                        "dataId": "day",
                        "label": "Point",
                        "color": [
                          130,
                          154,
                          227
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 10,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#FFC300",
                                    "#F1920E",
                                    "#E3611C",
                                    "#C70039",
                                    "#900C3F",
                                    "#5A1846"
                                ],
                                "reversed": True
                            },
                            "strokeColorRange": {
                                "name": "Global Warming",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#5A1846",
                                    "#900C3F",
                                    "#C70039",
                                    "#E3611C",
                                    "#F1920E",
                                    "#FFC300"
                                ]
                            },
                            "radiusRange": [
                                0,
                                50
                            ],
                            "filled": True
                        },
                        "hidden": False,
                        "textLabel": [
                            {
                                "field": None,
                                "color": [
                                    255,
                                    255,
                                    255
                                ],
                                "size": 18,
                                "offset": [
                                    0,
                                    0
                                ],
                                "anchor": "start",
                                "alignment": "center"
                            }
                        ]
                    },
                    "visualChannels": {
                        "colorField": {
                            "name": "WindSpd_ms-1",
                            "type": "real"
                        },
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": {
                            "name": "WindSpd_ms-1",
                            "type": "real"
                        },
                        "sizeScale": "sqrt"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "day": [
                            "time",
                            "WindSpd_ms-1"
                        ]
                    },
                    "enabled": True
                },
                "brush": {
                    "size": 0.5,
                    "enabled": False
                },
                "geocoder": {
                    "enabled": False
                },
                "coordinate": {
                    "enabled": False
                }
            },
            "layerBlending": "normal",
            "splitMaps": [],
            "animationConfig": {
                "currentTime": None,
                "speed": 1
            }
        },
        "mapState": {
            "bearing": 0,
            "dragRotate": False,
            "latitude": 41.87295484973828,
            "longitude": -87.63356380765224,
            "pitch": 0,
            "zoom": 11.80776433233219,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "dark",
            "topLayerGroups": {},
            "visibleLayerGroups": {
                "label": True,
                "road": True,
                "border": False,
                "building": True,
                "water": True,
                "land": True,
                "3d building": False
            },
            "threeDBuildingColor": [
                9.665468314072013,
                17.18305478057247,
                31.1442867897876
            ],
            "mapStyles": {}
        }
    }
}
