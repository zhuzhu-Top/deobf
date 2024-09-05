
这个项目是个binja插件

安装binja插件以及 workflow使用 自行了解

>样本就是 0xEEEE 大佬文章里的, 如果代码有问题,可以 提issue,我可能有的地方忘记改了

```angular2html
│   arch_hook.py  binja ArchitectureHook 案例
│   data.json     workflow需要读取信息的文件
│   data.py
│   de_br.py
│   dy_code.py
│   header_less.py 生成 data.json
│   LICENSE
│   new.bndb
│   plugin.json
│   README.md
│   symbolic_.py   符号执行(加点代码也可以生成data.json)
│   test.py
│   test_exe.py
│   triton_test.py
│   user_il.py
│   utils.py
│   work_flow.py   读取data.json 修改binja il
│   __init__.py

```



[workflow入口](https://github.com/zhuzhu-Top/deobf/blob/506eb3273f2c490946b24f9914fbf61bb14553a5/work_flow.py#L226)

这个函数最后两个调用
```python
recover_branch(func,procedure_addrs,jumps) 这里是修改 il 实现 cmp下沉
recover_blcok_flow(func,reg2values)        这里是把真实块直接跳转到下一个真实块
```