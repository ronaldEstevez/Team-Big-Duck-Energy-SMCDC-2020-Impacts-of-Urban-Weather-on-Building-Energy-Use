four = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "WindSpd_ms-1"
                  ],
                  "id": "clljlkvc",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1429444156500,
                      1429445062500
                  ],
                  "enlarged": False,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "WindSpd_ms-1",
                      "type": "real"
                  }
              },
                {
                  "dataId": [
                      "temp_K"
                  ],
                  "id": "p1r2no7b",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1429401600000,
                      1429402446000
                  ],
                  "enlarged": False,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "temp_K",
                      "type": "real"
                  }
              },
                {
                  "dataId": [
                      "Longwave_Wm-2"
                  ],
                  "id": "src5awrlp",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1429441588000,
                      1429442429000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "Longwave_Wm-2",
                      "type": "real"
                  }
              },
                {
                  "dataId": [
                      "RH_pct"
                  ],
                  "id": "hsrfyyjai",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1429443141000,
                      1429444155000
                  ],
                  "enlarged": False,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "RH_pct",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "xauu06s",
                    "type": "point",
                    "config": {
                        "dataId": "temp_K",
                        "label": "temp_points",
                        "color": [
                          241,
                          92,
                          23
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": False,
                        "visConfig": {
                            "radius": 30,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "ColorBrewer Reds-8",
                                "type": "singlehue",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#fff5f0",
                                    "#fee0d2",
                                    "#fcbba1",
                                    "#fc9272",
                                    "#fb6a4a",
                                    "#ef3b2c",
                                    "#cb181d",
                                    "#99000d"
                                ],
                                "reversed": False
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
                            "name": "temp_K",
                            "type": "real"
                        },
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear"
                    }
                },
                {
                    "id": "o1kistl",
                    "type": "point",
                    "config": {
                        "dataId": "WindSpd_ms-1",
                        "label": "wind_points",
                        "color": [
                          34,
                          63,
                          154
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": False,
                        "visConfig": {
                            "radius": 30,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "ColorBrewer Greens-8",
                                "type": "singlehue",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#f7fcf5",
                                    "#e5f5e0",
                                    "#c7e9c0",
                                    "#a1d99b",
                                    "#74c476",
                                    "#41ab5d",
                                    "#238b45",
                                    "#005a32"
                                ],
                                "reversed": False
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
                        "colorScale": "quantile",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear"
                    }
                },
                {
                    "id": "g5977v",
                    "type": "point",
                    "config": {
                        "dataId": "Longwave_Wm-2",
                        "label": "longwave_points",
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
                            "radius": 30,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "ColorBrewer Purples-8",
                                "type": "singlehue",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#fcfbfd",
                                    "#efedf5",
                                    "#dadaeb",
                                    "#bcbddc",
                                    "#9e9ac8",
                                    "#807dba",
                                    "#6a51a3",
                                    "#4a1486"
                                ]
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
                            "name": "Longwave_Wm-2",
                            "type": "real"
                        },
                        "colorScale": "quantile",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear"
                    }
                },
                {
                    "id": "xkt2tlv",
                    "type": "point",
                    "config": {
                        "dataId": "RH_pct",
                        "label": "humidity_points",
                        "color": [
                          18,
                          92,
                          119
                        ],
                        "columns": {
                            "lat": "lat",
                            "lng": "lon",
                            "altitude": None
                        },
                        "isVisible": False,
                        "visConfig": {
                            "radius": 30,
                            "fixedRadius": False,
                            "opacity": 0.5,
                            "outline": False,
                            "thickness": 2,
                            "strokeColor": None,
                            "colorRange": {
                                "name": "ColorBrewer Blues-8",
                                "type": "singlehue",
                                "category": "ColorBrewer",
                                "colors": [
                                    "#f7fbff",
                                    "#deebf7",
                                    "#c6dbef",
                                    "#9ecae1",
                                    "#6baed6",
                                    "#4292c6",
                                    "#2171b5",
                                    "#084594"
                                ]
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
                            "name": "RH_pct",
                            "type": "real"
                        },
                        "colorScale": "quantile",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "temp_K": [
                            "time",
                            "temp_K"
                        ],
                        "WindSpd_ms-1": [
                            "time",
                            "WindSpd_ms-1"
                        ],
                        "Longwave_Wm-2": [
                            "time",
                            "Longwave_Wm-2"
                        ],
                        "RH_pct": [
                            "time",
                            "RH_pct"
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
            "latitude": 41.87344707399566,
            "longitude": -87.62959294771424,
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
