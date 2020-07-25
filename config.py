map_1 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
              {
                  "id": "xdkpd8h",
                  "type": "point",
                  "config": {
                      "dataId": "Points",
                      "label": "Point",
                      "color": [
                        119,
                        110,
                        87
                      ],
                      "columns": {
                          "lat": "Lat",
                          "lng": "Lon",
                          "altitude": None
                      },
                      "isVisible": False,
                      "visConfig": {
                          "radius": 10,
                          "fixedRadius": False,
                          "opacity": 0.8,
                          "outline": False,
                          "thickness": 2,
                          "strokeColor": None,
                          "colorRange": {
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
                      "colorField": None,
                      "colorScale": "quantile",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear"
                  }
              },
                {
                  "id": "byu0va",
                  "type": "geojson",
                  "config": {
                      "dataId": "Footprint",
                      "label": "Footprint",
                      "color": [
                        23,
                        184,
                        190
                      ],
                      "columns": {
                          "geojson": "geometry"
                      },
                      "isVisible": True,
                      "visConfig": {
                          "opacity": 0.8,
                          "strokeOpacity": 0.8,
                          "thickness": 0.5,
                          "strokeColor": [
                              246,
                              209,
                              138
                          ],
                          "colorRange": {
                              "name": "Pink Wine",
                              "type": "sequential",
                              "category": "Uber",
                              "colors": [
                                  "#EDD1CA",
                                  "#E0B1B3",
                                  "#CF91A3",
                                  "#B77495",
                                  "#9A5B88",
                                  "#764476",
                                  "#50315E",
                                  "#2C1E3D"
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
                          "radius": 10,
                          "sizeRange": [
                              0,
                              10
                          ],
                          "radiusRange": [
                              0,
                              50
                          ],
                          "heightRange": [
                              0,
                              500
                          ],
                          "elevationScale": 5,
                          "stroked": False,
                          "filled": True,
                          "enable3d": False,
                          "wireframe": False
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
                          "name": "HGT_AGL",
                          "type": "real"
                      },
                      "colorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "heightField": None,
                      "heightScale": "linear",
                      "radiusField": None,
                      "radiusScale": "linear"
                  }
              }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Points": [
                            "BLDGID",
                            "MEAN_AVGHT",
                            "Lat",
                            "Lon"
                        ],
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "Heat_rejection"
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
            "latitude": 41.87730697735201,
            "longitude": -87.65683936830372,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

map_2 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
              {
                  "id": "6301vji",
                  "type": "geojson",
                  "config": {
                      "dataId": "Footprint",
                      "label": "Footprint",
                      "color": [
                        18,
                        147,
                        154
                      ],
                      "columns": {
                          "geojson": "geometry"
                      },
                      "isVisible": True,
                      "visConfig": {
                          "opacity": 0.8,
                          "strokeOpacity": 0.8,
                          "thickness": 0.5,
                          "strokeColor": [
                              221,
                              178,
                              124
                          ],
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
                          "radius": 10,
                          "sizeRange": [
                              0,
                              10
                          ],
                          "radiusRange": [
                              0,
                              50
                          ],
                          "heightRange": [
                              0,
                              500
                          ],
                          "elevationScale": 5,
                          "stroked": False,
                          "filled": True,
                          "enable3d": False,
                          "wireframe": False
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
                          "name": "Heat_rejection",
                          "type": "real"
                      },
                      "colorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "heightField": None,
                      "heightScale": "linear",
                      "radiusField": None,
                      "radiusScale": "linear"
                  }
              }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "Heat_rejection"
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
            "latitude": 41.87743091173837,
            "longitude": -87.65725030409813,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

map_22 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
              {
                  "id": "ct668wo",
                  "type": "geojson",
                  "config": {
                      "dataId": "Footprint",
                      "label": "Footprint",
                      "color": [
                          136,
                          87,
                          44
                      ],
                      "columns": {
                          "geojson": "geometry"
                      },
                      "isVisible": True,
                      "visConfig": {
                          "opacity": 0.8,
                          "strokeOpacity": 0.8,
                          "thickness": 0.5,
                          "strokeColor": [
                              255,
                              153,
                              31
                          ],
                          "colorRange": {
                              "name": "ColorBrewer Oranges-8",
                              "type": "singlehue",
                              "category": "ColorBrewer",
                              "colors": [
                                  "#fff5eb",
                                  "#fee6ce",
                                  "#fdd0a2",
                                  "#fdae6b",
                                  "#fd8d3c",
                                  "#f16913",
                                  "#d94801",
                                  "#8c2d04"
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
                          "radius": 10,
                          "sizeRange": [
                              0,
                              10
                          ],
                          "radiusRange": [
                              0,
                              50
                          ],
                          "heightRange": [
                              0,
                              500
                          ],
                          "elevationScale": 5,
                          "stroked": False,
                          "filled": True,
                          "enable3d": False,
                          "wireframe": False
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
                          "name": "Total_Elec",
                          "type": "real"
                      },
                      "colorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "heightField": None,
                      "heightScale": "linear",
                      "radiusField": None,
                      "radiusScale": "linear"
                  }
              }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "Total_Elec"
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
            "latitude": 41.87740211731931,
            "longitude": -87.65737229316757,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

map_3 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
              {
                  "id": "7sywi1in",
                  "type": "geojson",
                  "config": {
                      "dataId": "Footprint",
                      "label": "Footprint",
                      "color": [
                        241,
                        92,
                        23
                      ],
                      "columns": {
                          "geojson": "geometry"
                      },
                      "isVisible": True,
                      "visConfig": {
                          "opacity": 0.8,
                          "strokeOpacity": 0.8,
                          "thickness": 0.5,
                          "strokeColor": [
                              34,
                              63,
                              154
                          ],
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
                          "radius": 10,
                          "sizeRange": [
                              0,
                              10
                          ],
                          "radiusRange": [
                              0,
                              50
                          ],
                          "heightRange": [
                              0,
                              500
                          ],
                          "elevationScale": 5,
                          "stroked": False,
                          "filled": True,
                          "enable3d": False,
                          "wireframe": False
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
                          "name": "Total_NatG",
                          "type": "real"
                      },
                      "colorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "heightField": None,
                      "heightScale": "linear",
                      "radiusField": None,
                      "radiusScale": "linear"
                  }
              }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "Total_NatG"
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
            "latitude": 41.87742728880965,
            "longitude": -87.65747989289868,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

map_4 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "Footprint"
                  ],
                  "id": "abpby13r",
                  "name": [],
                  "type": None,
                  "value": None,
                  "enlarged": False,
                  "plotType": "histogram",
                  "yAxis": None
              }
            ],
            "layers": [
                {
                    "id": "dg39mw9",
                    "type": "geojson",
                    "config": {
                        "dataId": "Footprint",
                        "label": "Footprint",
                        "color": [
                          218,
                          112,
                          191
                        ],
                        "columns": {
                            "geojson": "geometry"
                        },
                        "isVisible": True,
                        "visConfig": {
                            "opacity": 0.8,
                            "strokeOpacity": 0.8,
                            "thickness": 0.5,
                            "strokeColor": [
                                18,
                                92,
                                119
                            ],
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
                            "radius": 10,
                            "sizeRange": [
                                0,
                                10
                            ],
                            "radiusRange": [
                                0,
                                50
                            ],
                            "heightRange": [
                                0,
                                500
                            ],
                            "elevationScale": 5,
                            "stroked": False,
                            "filled": True,
                            "enable3d": False,
                            "wireframe": False
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
                            "name": "HVAC_Elec_Intensity",
                            "type": "real"
                        },
                        "colorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "heightField": None,
                        "heightScale": "linear",
                        "radiusField": None,
                        "radiusScale": "linear"
                    }
                }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "HVAC_Elec_Intensity"
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
            "latitude": 41.87275609511713,
            "longitude": -87.65722014085111,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

map_5 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [],
            "layers": [
              {
                  "id": "f6xkk9g",
                  "type": "geojson",
                  "config": {
                      "dataId": "Footprint",
                      "label": "Footprint",
                      "color": [
                        77,
                        193,
                        156
                      ],
                      "columns": {
                          "geojson": "geometry"
                      },
                      "isVisible": True,
                      "visConfig": {
                          "opacity": 0.8,
                          "strokeOpacity": 0.8,
                          "thickness": 0.5,
                          "strokeColor": [
                              119,
                              110,
                              87
                          ],
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
                          "radius": 10,
                          "sizeRange": [
                              0,
                              10
                          ],
                          "radiusRange": [
                              0,
                              50
                          ],
                          "heightRange": [
                              0,
                              500
                          ],
                          "elevationScale": 5,
                          "stroked": False,
                          "filled": True,
                          "enable3d": False,
                          "wireframe": False
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
                          "name": "HVAC_Ngas_Intensity",
                          "type": "real"
                      },
                      "colorScale": "quantile",
                      "sizeField": None,
                      "sizeScale": "linear",
                      "strokeColorField": None,
                      "strokeColorScale": "quantile",
                      "heightField": None,
                      "heightScale": "linear",
                      "radiusField": None,
                      "radiusScale": "linear"
                  }
              }
            ],
            "interactionConfig": {
                "tooltip": {
                    "fieldsToShow": {
                        "Footprint": [
                            "BLDGID",
                            "HGT_AGL",
                            "Shape_Area",
                            "Area",
                            "HVAC_Ngas_Intensity"
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
            "latitude": 41.87745507341512,
            "longitude": -87.65730201562924,
            "pitch": 0,
            "zoom": 13.451941083083048,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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
                26.848523094644484,
                31.1442867897876,
                35.440050484930715
            ],
            "mapStyles": {}
        }
    }
}

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

feb20 = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "temp_K"
                  ],
                  "id": "kg5svz44r",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1424390400000,
                      1424391332000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "temp_K",
                      "type": "real"
                  }
              },
                {
                  "dataId": [
                      "WindSpd_ms-1"
                  ],
                  "id": "tlz8uz2gp",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1424390400000,
                      1424391332000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "WindSpd_ms-1",
                      "type": "real"
                  }
              },
                {
                  "dataId": [
                      "Longwave_Wm-2"
                  ],
                  "id": "nfytlok6h",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1424390400000,
                      1424391333000
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
                  "id": "5p5guo8a",
                  "name": [
                      "time"
                  ],
                  "type": "timeRange",
                  "value": [
                      1424390400000,
                      1424391334000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "yAxis": {
                      "name": "RH_pct",
                      "type": "integer"
                  }
              }
            ],
            "layers": [
                {
                    "id": "0s8kljd",
                    "type": "point",
                    "config": {
                        "dataId": "temp_K",
                        "label": "temperature",
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
                        "isVisible": True,
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
                    "id": "u8nl7q7",
                    "type": "point",
                    "config": {
                        "dataId": "WindSpd_ms-1",
                        "label": "wind speed",
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
                            "name": "WindSpd_ms-1",
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
                    "id": "18v9soj",
                    "type": "point",
                    "config": {
                        "dataId": "Longwave_Wm-2",
                        "label": "longwave radiation",
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
                        "colorScale": "quantize",
                        "strokeColorField": None,
                        "strokeColorScale": "quantile",
                        "sizeField": None,
                        "sizeScale": "linear"
                    }
                },
                {
                    "id": "11dqqwm",
                    "type": "point",
                    "config": {
                        "dataId": "RH_pct",
                        "label": "relative humidity",
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
                            "type": "integer"
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
            "latitude": 41.87432661396995,
            "longitude": -87.62825354482858,
            "pitch": 0,
            "zoom": 12.903882166166095,
            "isSplit": False
        },
        "mapStyle": {
            "styleType": "muted_night",
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

oct20 = {
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
                      1445299200000,
                      1445300126000
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
                      1445299200000,
                      1445300135000
                  ],
                  "enlarged": True,
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
                      1445299200000,
                      1445300132000
                  ],
                  "enlarged": False,
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
                      1445299200000,
                      1445300133000
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
                        "isVisible": True,
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
                        "isVisible": False,
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
            "styleType": "muted_night",
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

apr10 = {
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
                      1428624000000,
                      1428624933000
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
                      1428624000000,
                      1428624932000
                  ],
                  "enlarged": True,
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
                      1428624000000,
                      1428624933000
                  ],
                  "enlarged": False,
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
                      1428624000000,
                      1428624934000
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
                        "isVisible": True,
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
                        "isVisible": False,
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
            "styleType": "muted_night",
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

apr14 = {
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
                      1428969600000,
                      1428970532000
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
                      1428969600000,
                      1428970534000
                  ],
                  "enlarged": True,
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
                      1428969600000,
                      1428970533000
                  ],
                  "enlarged": False,
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
                      1428969600000,
                      1428970529000
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
                        "isVisible": True,
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
                        "isVisible": False,
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
            "styleType": "muted_night",
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
