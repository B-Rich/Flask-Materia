/** @jsx React.DOM */

var converter = new Showdown.converter();

var MarkdownEditor = React.createClass({
  getInitialState: function() {
    return {
      value: 'Type some *markdown* here!'
    };
  },
  handleChange: function() {
    this.setState({value: this.refs.textarea.getDOMNode().value});
  },
  componentDidMount: function() {
    console.log("!");
    $('.editor-textarea').autosize();
  },
  render: function() {
    return (
      <div className="MarkdownEditor">
        <div className="row">
          <div className="editor-input col s12 m6 l6">
            <h3>Input</h3>
            <textarea
              className="editor-textarea"
              onChange={this.handleChange}
              ref="textarea"
              defaultValue={this.state.value} />
          </div>

          <div className="editor-output col m6 l6 hide-on-small-only">
            <h3>Output</h3>
            <div
              className="content"
              dangerouslySetInnerHTML={{
                __html: converter.makeHtml(this.state.value)
              }}
            />
          </div>
        </div>
        <button className="btn waves-effect waves-light">Submit
          <i className="mdi-content-send right"></i>
        </button>
      </div>
    );
  }
});

React.renderComponent(MarkdownEditor({}), document.querySelector(".editor"))