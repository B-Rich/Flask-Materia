/** @jsx React.DOM */

var converter = new Showdown.converter();

var MarkdownEditor = React.createClass({
  getInitialState: function() {
    return {
      value: 'Type some *markdown* here!',
      cbValue: '0'
    };
  },
  handleChange: function() {
    this.setState({value: this.refs.textarea.getDOMNode().value});
  },
  checkboxChange: function() {
    this.setState({cbValue: event.target.value});
  },
  componentDidMount: function() {
    $('.editor-textarea').autosize();
  },
  render: function() {
    return (
      <div className="MarkdownEditor">
        <div className="row">
          <div className="input-field col s12">
            <input id="post_title" type="text" class="validate" />
            <label htmlFor="post_title">Post Title</label>
          </div>
          <div className="input-field col s12">
            <input id="flavor_text" type="text" class="validate" />
            <label htmlFor="flavor_text">Flavor Text (160 characters)</label>
          </div>
          <div className="input-field col s6">
            <input id="img_url" type="text" class="validate" />
            <label htmlFor="img_url">Image URL</label>
          </div>
          <div className="input-field col s6">
            <input id="categories" type="text" class="validate" />
            <label htmlFor="categories">Categories</label>
          </div>
        </div>
        <div className="row">
          <div className="editor-input col s12 m6 l6">
            <h5>Input</h5>
            <textarea
              className="editor-textarea"
              onChange={this.handleChange}
              ref="textarea"
              defaultValue={this.state.value} />
            <button className="btn waves-effect waves-light btn-submit">Submit
              <i className="mdi-content-send right"></i>
            </button>
          </div>

          <div className="editor-output col m6 l6 hide-on-small-only">
            <h5>Output</h5>
            <div
              className="content"
              dangerouslySetInnerHTML={{
                __html: converter.makeHtml(this.state.value)
              }}
            />
          </div>
        </div>
      </div>
    );
  }
});

React.renderComponent(MarkdownEditor({}), document.querySelector(".editor"))