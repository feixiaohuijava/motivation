$(function () {
	// console.log("start")

	//1.初始化Table
	var oTable = new TableInit();
	oTable.Init();

	//2.初始化Button的点击事件
	var oButtonInit = new ButtonInit();
	oButtonInit.Init();

});


var TableInit = function () {
	var oTableInit = new Object();
	//初始化Table
	oTableInit.Init = function () {
		$('#tb_departments').bootstrapTable('destroy');
		$('#tb_departments').bootstrapTable({
			url: '/getdata_mongodb/',         //请求后台的URL（*）
			method: 'get',                      //请求方式（*）
			toolbar: '#toolbar',                //工具按钮用哪个容器
			striped: true,                      //是否显示行间隔色
			cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
			pagination: true,                   //是否显示分页（*）
			sortable: true,                     //是否启用排序
			sortOrder: "asc",                   //排序方式
			//设置为undefined可以获取pageNumber，pageSize，searchText，sortName，sortOrder
			//设置为limit可以获取limit, offset, search, sort, order
			//queryParamsType:"undefined",
			queryParams: oTableInit.queryParams,//传递参数（*）
			sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
			pageNumber: 1,                       //初始化加载第一页，默认第一页
			pageSize: 5,                       //每页的记录行数（*）,当total<pageSize的时候，每页记录行数则为total了
			pageList: [5, 10, 25, 50, 100],        //可供选择的每页的行数（*）
			search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
			strictSearch: true,
			showColumns: true,                  //是否显示所有的列
			showRefresh: true,                  //是否显示刷新按钮
			minimumCountColumns: 2,             //最少允许的列数
			clickToSelect: true,                //是否启用点击选中行
			height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
			// responseHandler:function (res) {      //这个responseHandler如果注释，table中线条会不对齐
			// 	console.log(res)
			//     return res.DATA;
			// },
			uniqueId: "_id",                     //每一行的唯一标识，一般为主键列
			showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
			cardView: false,                    //是否显示详细视图
			detailView: false,                   //是否显示父子表
			columns: [{
                    checkbox : true
				},
				{
					field: 'Name',
					title: '召唤师',
				}, {
					field: 'ParentName',
					title: '部落'
				}, {
					field: 'Level',
					title: '角色'
				}, {
					field: 'Desc',
					title: '详情',
					width: '80px',
					events: operateEvents, //给按钮注册事件
					formatter: oTableInit.operate,//表格中增加按钮
				},]
		});
	};

	//得到查询的参数
	oTableInit.queryParams = function (params) {

		var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
			limit: params.limit,   //页面大小
			offset: params.offset,  //页码
			departmentname: $("#txt_search_departmentname").val(),
			search: params.search,
			order: params.order,
			ordername: params.sort,
			statu: $("#txt_search_statu").val()
		};
		console.log(temp)
		return temp;
	};

	oTableInit.operate = function () {
		console.log("start funciton operate")
		return [
			'<button id="TableEditor" type="button" class="btn btn-default">查看</button> &nbsp;&nbsp;',
			// '<img src="../static/fonts/81506654133_.pic.jpg" title="1" data-toggle="modal" data-target="#myModel" style=""/>'
		].join("")

	}
	window.operateEvents = { //添加一个按钮组在对应的按钮组中写下需要使用的事件
		"click #TableEditor": function (e, value, row, index) {//编辑按钮事件
			console.log("starting edit a button")
			// $("#myModal").html();
			$("#myModal").modal('show');
			setTimeout('$("#alertModalId").modal("hide")', 4000);
			$("#id-modal-body").bootstrapTable({
				url: '/showselect/',         //请求后台的URL（*）
				method: 'get',                      //请求方式（*）
				//toolbar: '#toolbar',                //工具按钮用哪个容器
				striped: true,                      //是否显示行间隔色
				cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
				//pagination: true,                   //是否显示分页（*）
				sortable: true,                     //是否启用排序
				sortOrder: "asc",                   //排序方式
				//设置为undefined可以获取pageNumber，pageSize，searchText，sortName，sortOrder
				//设置为limit可以获取limit, offset, search, sort, order
				//queryParamsType:"undefined",
				queryParams: detail_table(e,value,row,index),//传递参数（*）
				sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
				pageNumber: 1,                       //初始化加载第一页，默认第一页
				pageSize: 5,                       //每页的记录行数（*）,当total<pageSize的时候，每页记录行数则为total了
				pageList: [5, 10, 25, 50, 100],        //可供选择的每页的行数（*）
				//search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
				//strictSearch: true,
				//showColumns: true,                  //是否显示所有的列
				//showRefresh: true,                  //是否显示刷新按钮
				//minimumCountColumns: 2,             //最少允许的列数
				clickToSelect: true,                //是否启用点击选中行
				//height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
				// responseHandler:function (res) {      //这个responseHandler如果注释，table中线条会不对齐
				// 	console.log(res)
				//     return res.DATA;
				// },
				uniqueId: "_id",                     //每一行的唯一标识，一般为主键列
				//showToggle: true,                    //是否显示详细视图和列表视图的切换按钮
				cardView: false,                    //是否显示详细视图
				detailView: false,                   //是否显示父子表
				columns: [
					{
						field: 'team',
						title: '战队',
					},
					{
						field: 'honour',
						title: '荣誉',
					},]


			})
		}
	}



	function detail_table (e,value,row,index) {
		console.log(row) //获取的是父表格一行的数据
		console.log(row["Name"])
		return row["Name"]
	};


	return oTableInit;
};





var ButtonInit = function () {
	var oInit = new Object();
	var postdata = {};

	oInit.Init = function () {
		//初始化页面上面的按钮事件
	};

	return oInit;
};



