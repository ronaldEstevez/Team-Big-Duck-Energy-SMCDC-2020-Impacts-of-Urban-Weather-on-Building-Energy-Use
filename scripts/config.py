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
                        1424391540000,
                        1424392473000
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
                            "radius": 30,
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
                                30,
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
                        "sizeField": None,
                        "sizeScale": "linear"
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
            "latitude": 41.87348965518698,
            "longitude": -87.62208596192073,
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

dailyWindSpd = {
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
                      1431820800000,
                      1431821732000
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
                            "radius": 50,
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
                        "sizeField": None,
                        "sizeScale": "linear"
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
            "latitude": 41.872982551946365,
            "longitude": -87.63054598172721,
            "pitch": 0,
            "zoom": 13.172704837167547,
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

dailyShortWave = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "day"
                  ],
                  "id": "2lwjzrusq",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1431542129500,
                      1431543055500
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "Shortwave_Wm-2",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "15lvhye",
                    "type": "point",
                    "config": {
                        "dataId": "day",
                        "label": "Point",
                        "color": [
                          119,
                          110,
                          87
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
                            "name": "Shortwave_Wm-2",
                            "type": "real"
                        },
                        "colorScale": "quantize",
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
                        "day": [
                            "time",
                            "Shortwave_Wm-2"
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
            "latitude": 41.87253811746677,
            "longitude": -87.64015226470403,
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

dailyLongWave = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
                {
                    "dataId": [
                        "day"
                    ],
                    "id": "joqqedg5b",
                    "name": [
                        "time"
                    ],
                    "type": "timeRange",
                    "value": [
                        1431734400000,
                        1431735331000
                    ],
                    "enlarged": True,
                    "plotType": "lineChart",
                    "yAxis": {
                        "name": "Longwave_Wm-2",
                        "type": "real"
                    }
                }
            ],
            "layers": [
                {
                    "id": "melmnws",
                    "type": "point",
                    "config": {
                        "dataId": "day",
                        "label": "Point",
                        "color": [
                          221,
                          178,
                          124
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
                        "colorScale": "quantize",
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
                        "day": [
                            "time",
                            "Longwave_Wm-2"
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
            "latitude": 41.87355943701317,
            "longitude": -87.63886146325068,
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
