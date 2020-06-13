# Change the behavior of google.colab.data_table to my liking
from IPython.display import Javascript, clear_output
from google.colab.output import eval_js

# First, 
# = %load_ext google.colab.data_table
get_ipython().run_line_magic('load_ext', 'google.colab.data_table')
# Then, make the default width to fit content, instead of 100%
from google.colab.data_table import DataTable
DataTable.min_width = '0'
DataTable.max_rows = 35000


def unload():
    """Unload the data_table extension"""
    get_ipython().run_line_magic('unload_ext', 'google.colab.data_table')


def filter_df(df):
    """Desplay the dataframe and let user select rows"""
    display(DataTable(df, min_width='300'))
    display(Javascript('''
      var bag = new Set([])
      function show_checkboxes(){
        var cells = document.querySelectorAll('td.index_column')
        for (c of cells) {
          var v = c.classList[2]  // "id-0"
          var cb = checkbox(v, bag.has(v))
          c.append(cb)
        }
        var nums = document.querySelector('.google-visualization-table-page-numbers')
        if (nums) nums.onclick = show_checkboxes  // ต้องดักใหม่ทุกครั้ง
      }
      function checkbox(value, checked=false) {
        cb = document.createElement('input')
        cb.type = 'checkbox'
        cb.value = value
        cb.checked = checked
        cb.onchange = update_bag
        return cb
      }
      function update_bag(){
        var cb = event.target
        if (cb.checked) {
          bag.add(cb.value)
        } else {
          bag.delete(cb.value)
        }
        console.log(bag)
      }
      function show_return_button(){
        var b = document.createElement('button')
        b.id = 'return'
        b.innerHTML = 'Return'
        document.querySelector('#output-body').append(b)
      }
      show_checkboxes()
      show_return_button()

      var result = new Promise(resolve =>{
        var button = document.getElementById('return')
        button.onclick = ()=>{
          resolve([...bag]) // convert to list
        }
      })
    '''))
    bag = eval_js('result')
    clear_output()
    ids = [int(v[3:]) for v in bag]
    return df.iloc[ids]