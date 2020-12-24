# AlienAndWarcraft
《Python编程：从入门到实践》第一个小项目，外星人大战。本仓库有两个分支，master为书里原版的个人简单修改。developer为开发版本，主要计划做美化以及游戏逻辑，可能会重构代码结构。

## master分支与原版区别
1. 修改了计分板文件scoreboard，增加代码复用。个人设计是，计分板是一块完整的面板，其中分割为不同部分。

2. 增加了最大帧率。原作没有这个是个很大的遗憾，很简单但能大幅度提高游戏的可玩性和完整性。

3. 一些小改动，例如注释，部分方法的实现，还有部分函数间关系的逻辑（主要有些部分没看书自己写的，后面就发现有出入，干脆按自己想法写了）

4. 去掉了最高分和剩余飞船数量显示（懒），稍微改了下计分板布局。

## master分支后续计划
1. 重构代码：部分代码依旧复用性不好，冗余，组织上也稍乱。

2. 增加一个系统些的比较，例如框架整理，常用方法

## developer分支计划
1.美化工作
  1. 替换背景
  
  2. 令背景滚动
  
  3. 替换飞船、外星人、子弹图标
  
  4. 增加爆炸特效
  
  5. 修改计分板图标和显示效果


2.游戏逻辑
  1. 外星人增加速度属性，令它们与窗口做完全弹性碰撞
  
  2. 每行不再排满外星人，而是按一定分布，随机个数
  
  3. 外星人的掉落不是直线/折线, 而是一定的函数曲线
  
  4. 外星人掉落速度不再一致
  
  5. 升级后的子弹可增加碰撞体积和外观
  
  6. 增加部分精英/boss外星人，让子弹和外星人都有数值，不同外星人需要不同数量的子弹