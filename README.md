# geoJson-cn

python爬虫获取中国-省-市-区县的geoJSON格式地图数据

爬取日期： 2021-02-05

对应文件夹解释:
```txt
mapdata
├── area-code
│   ├── index.json 区域数据索引
│   ├── china-area.json 中国地图三级行政区域地图结构信息
│   └── world-area-cn.json 世界地图数据结构定义
├── china
│   ├── china.json 中国地区包含子区域
│   ├── city 各市地图-包含子区域
│   └── province 各省地图-包含子区域
├── world
│   ├── world-cn.json 世界地图，按国家划分，中文国家地名
│   └── world-continents.json 世界地图，按大洲划分，英文大洲名
└── infos.json 中国地区区域列表

```

数据来源： http://datav.aliyun.com/tools/atlas/