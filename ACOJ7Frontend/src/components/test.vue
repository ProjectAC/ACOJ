<template>
  <div>
		<h1>大乌龟找妈妈</h1>
    {{ parseInt(a) + parseInt(b) }}<br/>
    <slot></slot>
    <div id="body" class="greyBlock">
		<p>找啊找，找不到，东找找，西找找，都在哪里呀？？？</p>
		<p>hint:flag由多部分组成，几部分？乌龟几部分就是几部分。本题意在考察收集信息的能力。</p>
		<!--Good Job! The first part is AAA{, the next part is also in this page, but maybe it has been encoded? Try to search for it!-->
    </div>
	</div>
</template>

<script>
export default {
  props: [
    'a',
    'b'
  ]
}
</script>
<style scoped>

/*
.greyBlock{
  border-radius: 5px;
  background-color: #00fcff;
  padding: 20px 20px 20px 20px;
}*/

</style>