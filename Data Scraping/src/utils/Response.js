class Response {
  constructor(success, data, message) {
    this.success = success;
    this.data = data;
    this.message = message;
  }

  createResponse() {
    return {
        success: this.success,
        data: this.data,
        message: this.message,
    };
  }
}


module.exports = Response;